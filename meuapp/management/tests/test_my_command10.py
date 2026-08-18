"""testa o menu interativo do my_command10, mockando input() e o client do ACR"""
from unittest.mock import MagicMock, patch

from meuapp.management.commands import my_command10


def _run_main(inputs):
    with patch("builtins.input", side_effect=inputs):
        my_command10.main()


def test_list_repositories(capsys):
    mock_client = MagicMock()
    mock_client.list_repository_names.return_value = ["repo1", "repo2"]

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client):
        _run_main(["https://test.azurecr.io", "1", "3"])

    output = capsys.readouterr().out
    assert "repo1" in output
    assert "repo2" in output
    mock_client.list_repository_names.assert_called_once()


def test_delete_manifest_when_repo_exists(capsys):
    mock_client = MagicMock()
    mock_client.list_repository_names.return_value = ["repo1", "repo2"]

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client):
        _run_main(["https://test.azurecr.io", "2", "repo1", "sha256:abc", "nao", "3"])

    mock_client.delete_manifest.assert_called_once_with("repo1", "sha256:abc")
    assert "repo1 deleted with sucess." in capsys.readouterr().out


def test_delete_manifest_when_repo_not_found(capsys):
    mock_client = MagicMock()
    mock_client.list_repository_names.return_value = ["repo1", "repo2"]

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client):
        _run_main(["https://test.azurecr.io", "2", "repo-nao-existe", "sha256:abc", "3"])

    mock_client.delete_manifest.assert_not_called()


def test_invalid_menu_option(capsys):
    mock_client = MagicMock()

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client):
        _run_main(["https://test.azurecr.io", "9", "3"])

    assert "option invalid,try again." in capsys.readouterr().out


def test_non_numeric_menu_option(capsys):
    mock_client = MagicMock()

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client):
        _run_main(["https://test.azurecr.io", "abc", "3"])

    assert "apenas 1,2 ou 3." in capsys.readouterr().out


def test_menu_repeats_without_asking_for_url_again():
    mock_client = MagicMock()
    mock_client.list_repository_names.return_value = ["repo1", "repo2"]

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(my_command10, "ContainerRegistryClient", return_value=mock_client) as ctor:
        _run_main([
            "https://test.azurecr.io", "1", "2", "repo1", "sha256:abc", "nao", "3",
        ])

    assert ctor.call_count == 1


def test_connection_error_retries_with_new_url(capsys):
    mock_client = MagicMock()

    with patch.object(my_command10, "DefaultAzureCredential", return_value=MagicMock()), \
         patch.object(
             my_command10,
             "ContainerRegistryClient",
             side_effect=[ValueError("bad url"), mock_client],
         ):
        _run_main(["url-invalida", "https://test.azurecr.io", "3"])

    assert "error in connection:bad url" in capsys.readouterr().out

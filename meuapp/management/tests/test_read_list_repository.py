"""fazendo teste para ver se realmente a funcao faz a responsabilidade dela"""
from unittest.mock import MagicMock, patch

from meuapp.management.commands import my_command09
from meuapp.management.commands.my_command09 import read_list_repositorys


def test_read_list_repository_in_acr():
    result = read_list_repositorys()
    assert result


def test_read_list_repository_with_mock():
    mock_client = MagicMock()
    mock_client.list_repository_names.return_value = ["repo1", "repo2"]

    with patch.object(my_command09, "client", mock_client):
        result = read_list_repositorys()

    assert list(result) == ["repo1", "repo2"]
    mock_client.list_repository_names.assert_called_once()

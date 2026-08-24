from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ResourceNotFoundError


def azure_auth() -> DefaultAzureCredential:
    try:
        return DefaultAzureCredential()
    except Exception as error:
        print(f"error in credential:{error}")
        return None


def regisry_client(url: str, credential: DefaultAzureCredential) -> ContainerRegistryClient:
    try:
        return ContainerRegistryClient(url, credential)
    except ValueError as error:
        print(f"error in connection:{error}")
        return None


def main_options() -> str:
    print("Opções")
    print("1 - Listar imagens")
    print("2 - Deletar imagem")
    print("3 - Sair")
    option = input("Escolha uma opção: ")

    if option not in ["1", "2", "3"]:
        print("Opção inválida. Tente novamente.")
        return main_options()

    return option


def list_images(client: ContainerRegistryClient):
    try:
        repositories = client.list_repository_names()
        for i in repositories:
            print(i)
    except Exception as error:
        print(f"error in list repository:{error}")


def delete_image(client: ContainerRegistryClient, repository: str, tag: str):
    try:
        client.delete_manifest(repository, tag)
        print(f"{repository}:{tag} deleted with success.")
    except ResourceNotFoundError:
        print(f"Image {repository}:{tag} not found.")
    except Exception as error:
        print(f"error in delete image:{error}")
        return

    client.delete_manifest(repository, tag)


def main():
    auth = azure_auth()
    if not auth:
        print("User not authenticated. Please check your Azure credentials.")
        return

    url = input("Digite a URL do registro de contêiner: ").strip()
    client = ContainerRegistryClient(url, auth)

    while True:
        option = main_options()

        # List images
        if option == "1":
            list_images(client)

        # Delete image
        elif option == "2":
            repository = input("Digite o nome do repositório: ").strip()
            tag = input("Digite a tag da imagem: ").strip()
            delete_image(client, repository, tag)

        # Exit
        elif option == "3":
            return


if __name__ == "__main__":
    main()
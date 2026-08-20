from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ResourceNotFoundError

def menu():
    print("Escolha uma opcao abaixo: ")
    print("1-Listar images: ")
    print("2-Deletar images: ")
    print("3-Sair")
    print("4-Saudação: ")

def saudacao():
    nome = input("Insira seu nome: ").strip()
    msg = f"Olá {nome} seja bem-vindo ao meu sistema!"
    print(msg)

def validate_url(url:str):
    if not url:
        return False
    if not url.startswith("https://"):
        return False
    if not url.endswith(".azurecr.io"):
        return False
    return True

def registry_client(url:str,credential: DefaultAzureCredential) -> ContainerRegistryClient:
    try:
     return ContainerRegistryClient(url, credential)
    except ValueError as error:
        print(f"error in connection:{error}")
        return None

def azure_auth() -> DefaultAzureCredential:
    try:
        return DefaultAzureCredential()
    except Exception as error:
        print(f"Error in credentials: {error}")
        return None

def list_images(client: ContainerRegistryClient):
    try:
        repositories = client.list_repository_names()
        for repository in repositories:
            print(repository)
    except Exception as error:
        print(f"{error}")

def delete_images(client: ContainerRegistryClient, repository: str, tag: str):
    try:
        client.delete_manifest(repository, tag)
        print(f"Delete feito {repository}:{tag}")
    except ResourceNotFoundError:
        print(f"{repository} nao encontrado")
    except Exception as error:
        print(f"Erro ao deletar {error}")

def main():
    authenticator = azure_auth()
    b = 1
    url = input("Digite uma url: ").strip()
    if not validate_url(url):
        print("URL invalida.")
        return
    client = registry_client(url, authenticator)
    if client is None:
        print("Nao foi possivel conectar ao registry.")
        return
    while b == 1:
        menu()
        opcao = input("Insira uma opcao: ")
        if opcao == "1":
            list_images(client)
        elif opcao == "2":
            repository = input("Insira um repository: ")
            tag = input("Insira uma tag ou digest: ")
            delete_images(client, repository, tag)
        elif opcao == "3":
            print("Saindo...")
            b = 0
        elif opcao == "4":
            saudacao()
        else:
            print("Opcao invalida.")
main()
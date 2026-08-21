from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ResourceNotFoundError
# https://devnatanrcs.azurecr.io

def menu():
    print("Escolha uma opcao abaixo: ")
    print("1-Listar images: ")
    print("2-Deletar images: ")
    print("3-Sair")
    print("4-Saudação: ")
    print("5-Teste")

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
    return ContainerRegistryClient(url,credential)

def azure_auth() -> DefaultAzureCredential:
    return DefaultAzureCredential()

def list_images(client: ContainerRegistryClient):
    try:
        repositories = client.list_repository_names()
        for repository in repositories:
            print(repository)
    except Exception as error:
        print(f"{error}")



def delete_manifest(client: ContainerRegistryClient,repository: str, digest: str):
    try:
        client.delete_manifest(repository,digest)
        print(f"{repository}:{digest} deletado com sucesso!")
    except ResourceNotFoundError:
        print(f"{repository}:{digest} nao encontrado.")
    except Exception:
        print(f"{repository}:{digest} nao foi possivel deletar!")


def list_tags(client: ContainerRegistryClient, repository: str):
    try:
        tags = client.list_tag_properties(repository)
        for tag in tags:
            print(f"{tag.name}")
            print(f"{tag.digest}")
        option = input("Oque deseja excluir tag ou digest: ")
        if option == "tag":
            tag_nome = input("Insira a tag: ").strip()
            if not tag_nome:
                print(f"{tag_nome} vazia ou nao encontrada.")
            client.delete_tag(repository,tag_nome)
            print(f"{repository}:{tag_nome} deletado com sucesso.")
        elif option == "digest":
            digest = input("Insira um digest: ")
            if not digest:
                print(f"{digest} vazio ou nao encontrado.")
            client.delete_manifest(repository,digest)
            print(f"{repository}:{digest} deletado com sucesso")
        else:
            print(f"Error,{option} invalido")
    except ResourceNotFoundError:
        print(f"Nenhum {repository} encontrado")
    except Exception:
        print(f"Erro ao deletar {repository}")
        

def main():
    b = 1
    url = input("Digite uma url: ").strip()
    if not validate_url(url):
        print("URL invalida.")
        return
    try:
        authenticator = azure_auth()
        client = registry_client(url, authenticator)
    except ValueError as error:
        print(f"Error ao criar o Client: {error}")
    while b == 1:
        menu()
        opcao = input("Insira uma opcao: ")
        if opcao == "1":
            list_images(client)
        elif opcao == "2":
            repository = input("Insira um repo: ")
            list_tags(client,repository)
        elif opcao == "3":
            print("Saindo...")
            b = 0
        elif opcao == "4":
            saudacao()
        else:
            print("Opcao invalida.")
main()


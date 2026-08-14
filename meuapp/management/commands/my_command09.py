"""Script para listar minhas images do ACR e deletar manifest"""
from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential

endpoint_the_url= "https://devnatanrcs.azurecr.io"
credential= DefaultAzureCredential()
try:
    client= ContainerRegistryClient(endpoint_the_url,credential)
except ValueError as error:
    print(f"error in connection {error}")


def read_list_repositorys():
    for all_repository in client.list_repository_names():
        print(f"all repository in acr: {all_repository}")

if __name__ == "__main__":
    read_list_repositorys()


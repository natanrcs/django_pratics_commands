"""Script para listar minhas images do ACR e deletar manifest"""
from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential

endpoint_url= "https://devnatanrcs.azurecr.io" 
credential= DefaultAzureCredential()
try:
    client= ContainerRegistryClient(endpoint_url,credential)
except ValueError as error:
    raise ValueError(f"invalid client configuration: {error}") from error



def list_repositories():
    repositories= client.list_repository_names()
    for repository in repositories:
        print(repository)
    return repositories

if __name__ == "__main__":
    list_repositories()
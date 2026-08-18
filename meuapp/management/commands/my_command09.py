"""Script para listar minhas images do ACR e deletar manifest"""
from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError
endpoint_url="https://devnatanrcs.azurecr.io" 
credential= DefaultAzureCredential()

try:
    client= ContainerRegistryClient(endpoint_url,credential)
except ValueError as error:
    raise ValueError(f"invalid client configuration: {error}") from error


def delete_manifest(repository,digest):
    try:
        client.delete_manifest(repository,digest)
        print(f"manifest deleted sucess:{repository}")
    except HttpResponseError as error:
        raise HttpResponseError(message=f"error in delete manifest {error}") from error


if __name__ == "__main__":
    delete_manifest("alpine","")

from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ResourceNotFoundError
credential = DefaultAzureCredential()
#  https://devnatanrcs.azurecr.io
while True:
    url = input("digite uma url meu parça: ").lower().strip()
    try:
        client = ContainerRegistryClient(url,credential)
    except ValueError as error:
        print(f"error in connection:{error}")
        continue
    try:
        chose = int(input("escolha: 1-listar imagem ou 2-deletar imagem ou 3-para sair: "))
        if chose == 1:
            try:
                repositories = client.list_repository_names()
                for i in repositories:
                    print(i)
            except Exception as error:
                print(f"error in list repository:{error}")
        elif chose == 2:
            try:
                repositories = client.list_repository_names()
                repo = input("digite um repository: ")
                tag = input("digite uma tag: ")
                for i in repositories:
                    if repo == i:
                        client.delete_manifest(repo,tag)
                        print(f"{i} deleted with sucess.")
                        for j in range(1):
                            b = input("deseja continuar? ")
                            if b == "sim":
                                continue
                            else:
                                print("encerrando...")
                                break
            except Exception as error:
                print(f"error in {error}")
        elif chose == 3:
            msg = f"exit inté..!"
            print(msg)
            break
        else:
            print("option invalid,try again.")
    except ValueError:
        print("apenas 1,2 ou 3.")
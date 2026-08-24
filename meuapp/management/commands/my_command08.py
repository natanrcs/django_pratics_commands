#Desafio do cep em programacao orientada a objetos
import requests
from pprint import pformat
class Cep():
    def __init__(self,cep: str):
        self.cep = cep.replace("-","").strip()

    def validar_cep(self):
        if len(self.cep) != 8:
            return "O cep deve conter 8 digitos"
        return "Cep válido! tudo certo!"

    def buscar_infos_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        response = requests.get(url,timeout=15)
        if response.status_code == 200:
            data = pformat(response.json())
            return f"Os dados do seu cep são: {data}"
        else:
            return f"Erro ao consultar {self.cep},nenhum dados retornados!"

    def teste(self):
        return f"Meu cep de casa é: {self.cep}"

my_cep_home= Cep("06149-203")
cep2= Cep("01001-000")
print(my_cep_home.validar_cep())
print(my_cep_home.buscar_infos_cep())
print(my_cep_home.teste())
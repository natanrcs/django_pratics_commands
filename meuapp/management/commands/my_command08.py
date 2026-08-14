"""fazendo o mesmo desafio sem framework"""
"""consulta no azure,lista todas as imagens do acr,quais libs se conecta ao azure"""
import argparse
import requests
from pprint import pformat

def main():
    parser= argparse.ArgumentParser(description="Desafio do Pablito script sem Framework!")
    parser.add_argument("--cep",type=str,required=True)
    parser.add_argument("--natan",type=str,required=True)
    arguments= parser.parse_args()
    cep= arguments.cep.replace("-","").strip()
    url=f"https://viacep.com.br/ws/{cep}/json/"
    if len(cep) != 8 or not cep.isdigit():
        messager_error= f"error: cep deve contem 8 digitos"
        print(messager_error)
    try:
        requi= requests.get(url,timeout=15)
        if requi.status_code ==200:
            dados=requi.json()
            results= {"cep": dados["cep"],"logradouro": dados["logradouro"],"local": dados["localidade"],"bairro": dados["bairro"],"uf": dados["uf"],"ibge": dados["ibge"]}
            format= pformat(results)
            print(f"{format}")
    except requests.RequestException as error:
        print(f"error in request:{error}")

if __name__ == "__main__":
    main()

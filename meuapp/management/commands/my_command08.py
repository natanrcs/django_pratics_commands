"""fazendo o mesmo desafio sem framework"""
import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="fazendo desafio do pablo sem frame-work")
    parser.add_argument("--cep",type=str,required=True,default=True)
    parser.add_argument("--natan",type=str,required=True,default=True)

    args = parser.parse_args()
    cep= args.cep.replace("-","").strip()
    url= f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resq= requests.get(url)
        if resq.status_code == 200:
            data= resq.json()
            result={
                "cep": data.get("cep"),
                "logradouro": data.get("logradouro"),
                "bairro": data.get("bairro"),
                "uf": data.get("uf"),
                "regiao": data.get("regiao"),
                "ibge": data.get("ibge")
            }
            print(f"result in request: {result}")
        else:
            print(f"error in request:{resq.status_code}")
    except ValueError as error:
        print(f"error in connection:{error}")

if __name__ == "__main__":
    print("fiz sozinho")
    main()
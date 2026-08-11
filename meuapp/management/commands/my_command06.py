"""fazendo o mesmo desafio sem framework"""
import argparse
from pprint import pformat

def main():
    parser = argparse.ArgumentParser(description="fazendo desafio do pablo sem frame-work")
    parser.add_argument("--dev-backend",type=str)
    parser.add_argument("--cafe",type=str)
    parser.add_argument("--empresa")
    parser.add_argument("--testando",type=str)
    my_args = parser.parse_args()
    result ={
        "quem_é": my_args.dev_backend,
        "cafe": my_args.cafe,
        "empresa": my_args.empresa,
        "teste": my_args.testando}
    data_response = pformat(result)
    print(data_response)

if __name__ == "__main__":
    print("fiz sozinho")
    main()
    
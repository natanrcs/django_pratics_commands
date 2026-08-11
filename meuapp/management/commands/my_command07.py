from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "Desafio consulta CEP"

    def add_arguments(self, parser):
        parser.add_argument("--cep", type=str, required=True)

    def handle(self, *args, **options):
        cep = options.get("cep").replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                data = response.json()
                text = {
                    "cep": data.get("cep"),
                    "logradouro": data.get("logradouro"),
                    "bairro": data.get("bairro"),
                    "localidade": data.get("localidade"),
                    "ibge": data.get("ibge")
                }
                self.stdout.write(self.style.SUCCESS(f"{text}"))
            else:
                self.stdout.write(self.style.ERROR(f"Erro na requisição: {response.status_code}"))
        except requests.exceptions.RequestException as error:
            self.stdout.write(self.style.ERROR(f"Erro na conexão: {error}"))
                

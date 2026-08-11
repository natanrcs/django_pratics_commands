from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "Consumindo uma URL"

    def handle(self, *args, **kwargs):
        url = "https://portaldoadmin.serveblog.net/api/payments/about"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                fizsozinho = "fiz sozinho"
                data = response.json()
                self.stdout.write(self.style.SUCCESS(f"return in request: {data}, {fizsozinho}"))
            else:
                self.stdout.write(self.style.ERROR(f"error in request:{response.status_code}"))
        except ValueError as e:
            messager_error = f"error in consumer url:{e}"
            self.stdout.write(self.style.ERROR(messager_error))
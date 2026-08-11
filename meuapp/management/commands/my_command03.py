from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Processa alguma lógica e informa o resultado"

    def handle(self, *args, **kwargs):
        total_processado = 0
        erros = 0
        for i in range(1,101):
            if i % 2 == 0:
                total_processado += 1
            else:
                erros += 1
        mensagem = f"total_de_par: {total_processado},total_de_impar: {erros}"
        self.stdout.write(self.style.SUCCESS(mensagem))

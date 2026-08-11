from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Comando de boas-vindas"

    def handle(self, *args, **kwargs):
        name = "Dev Natan Ramos"
        mensagem_do_dia = f"Seja Bem-vindo {name},Comando executado com sucesso!"
        self.stdout.write(self.style.SUCCESS(mensagem_do_dia))
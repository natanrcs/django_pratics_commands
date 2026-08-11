from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "teste"

    def add_arguments(self, parser):
        parser.add_argument("--testando-nome",type=str)

    def handle(self, *args, **options):
        name_test= options.get("testando-nome")
        self.stdout.write(self.style.SUCCESS(f"fiz sozinho o teste: olá Dev:{name_test}"))
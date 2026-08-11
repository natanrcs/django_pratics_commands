from django.core.management.base import BaseCommand
from pprint import pformat
"""
Input 
python manage.py manage_azure_container_registry_so \
  --azure-client-id principaliphone \              
  --azure-client-secret telefonica \                       
  --azure-client-tenant-id tenantcelular \   
  --registry-endpoint https://xxx.azurecr.io \
  --repository chocolate \    

Output
Id:principaliphone
secret:telefonica
tenant:tenantcelular
registry: https://xxx.azurecr.io
repository:chocolate
fiz sozinho
"""
class Command(BaseCommand):
    help = "Comando para teste "

    def add_arguments(self, parser):
        parser.add_argument("--azure-client-id",type=str)
        parser.add_argument("--azure-client-secret",type=str)
        parser.add_argument("--azure-tenant-id",type=str)
        parser.add_argument("--registry-endpoint",type=str)
        parser.add_argument("--repository",type=str)

    def handle(self, *args, **options):
        client_id = options.get("azure_client_id")       
        client_secret = options.get("azure_client_secret") 
        client_tenant = options.get("azure_tenant_id")      
        client_registry = options.get("registry_endpoint")
        repository = options.get("repository") 
        response= {"id":client_id,"secret":client_secret,"tenant":client_tenant,"registry": client_registry,"repository":repository}
        response_json = pformat(response)
        self.stdout.write(self.style.SUCCESS(f"fiz sozinho: {response_json}"))
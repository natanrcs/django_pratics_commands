"""fazendo teste para ver se realmente a funcao faz a responsabilidade dela"""
from management.commands.my_command09 import read_list_repositorys
def test_read_list_repository_in_acr():
    result= read_list_repositorys()
    assert isinstance(result)
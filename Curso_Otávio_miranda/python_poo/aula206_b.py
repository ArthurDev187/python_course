import json
from aula206_a import Pessoa, CAMINHO_ARQUIVO
lista_pessoas = {}
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    
    for indice, pessoa in enumerate(pessoas):
        lista_pessoas[f'pessoa_{indice+1}'] = pessoa
    
print(lista_pessoas)

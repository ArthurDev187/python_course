# Exercício - Salve sua classe em Json
# Salve sua classe em Json e depois crie novamente as instâncias
# da classe com os dados salvos, Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'python_poo\\aula206.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('Arthur', 28)
p2 = Pessoa('islaine', 31)
p3 = Pessoa('Zayan', 2)

pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as file:
    json.dump(pessoas, file, ensure_ascii=False, indent=2)
    
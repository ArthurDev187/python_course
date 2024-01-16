# Atributos de classes
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def data_nascimento(self):
        return Pessoa.ano_atual - self.idade 
    

p1 = Pessoa('Arthur', 28) 
p1_nascimento = p1.data_nascimento()
print(f'{p1.nome} tem {p1.idade} e nasceu no ano de {p1_nascimento}')

p2 = Pessoa('Silas', 22) 
p2_nascimento = p2.data_nascimento()
print(f'{p2.nome} tem {p2.idade} e nasceu no ano de {p2_nascimento}')
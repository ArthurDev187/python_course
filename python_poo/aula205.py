# __dict__ e vars para atributos de instâncias
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def gerar_data_nascimento(self):
        return Pessoa.ano_atual - self.idade 
    

p1 = Pessoa('Arthur', 28)
print(p1.__dict__)
print(vars(p1))
print()

dados = {'nome': 'Stefani', 'idade': 28}

p2 = Pessoa(**dados) 
print(p2.__dict__)
print(vars(p2)) 

# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja 
# ao invés de receber a instância no primeiro parâmetro
# receberemos a própria classe.
class Pessoa:
    ano = 2023 # atributo da classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    @classmethod
    def gera_com_idade_50(cls, nome):
        return cls(nome, 50)
    
    
    @classmethod
    def gera_sem_nome(cls, idade):
        return cls('Anônimo', idade)
    
    
p1 = Pessoa('Arthur', 28) 
p2 = Pessoa.gera_com_idade_50('Amélia')
p3 = Pessoa.gera_sem_nome(34)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

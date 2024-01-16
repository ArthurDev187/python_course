# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('Falar_nome está em classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
    

class Cliente(Pessoa):
    cpf = 'CPF está em cliente agora.'
    def falar_nome_classe(self):
        print('Falar_nome está em classe CLIENTE.')
        print(self.nome, self.sobrenome, self.__class__.__name__)
    

class Aluno(Pessoa):
    def falar_nome_classe(self):
        print('Falar_nome está em classe ALUNO.')
        print(self.nome, self.sobrenome, self.__class__.__name__)
    

c1 = Cliente('arthur', 'Rodrigues') 
a1 = Aluno('Islaine', 'Rodrigues') 
c1.falar_nome_classe()
a1.falar_nome_classe()
print(c1.cpf)
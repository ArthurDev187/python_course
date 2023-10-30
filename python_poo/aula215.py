# Exercício com classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Fabricante (nome)
# 3 - Crie uma classe Motor (nome)
# 4 - Faça uma ligação entre Carro tem um motor
# Obs: Motor pode ser de vários carros
# 5 - Faça uma ligação ente Carro e Fabricante
# Obs: Fabricante pode ter vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._fabricante = None
        self._motor = None
        
    def insere_motor(self, nome_motor):
        self._motor = nome_motor 
    
    def insere_fabricante(self, nome_fabricante):
        self._fabricante = nome_fabricante
    
    def mostrar_dados_carro(self):
        print(f'Modelo carro: {self._nome}') 
        print(f'Motor: {self._motor._nome}') 
        print(f'Fabricante: {self._fabricante._nome}')
    

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
    

class Motor:
    def __init__(self, nome):
        self._nome = nome


carro1 = Carro('fusca') 
motor1 = Motor('Motor de Ferrari') 
motor2 = Motor('Motor de Machlareen')
fabricante1 = Fabricante('Porshe') 

carro1.insere_fabricante(fabricante1) 
carro1.insere_motor(motor1)
carro1.insere_motor(motor2)
carro1.mostrar_dados_carro()


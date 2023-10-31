# Exercício com classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Fabricante (nome)
# 3 - Crie uma classe Motor (nome)
# 4 - Faça uma ligação entre Carro tem um motor
# Obs: Motor pode ser de vários carros
# 5 - Faça uma ligação ente Carro e Fabricante
# Obs: Fabricante pode ter vários carros
# Exiba o nome do carro, motor e fabricante na tela
# Eu vou refazer o exercício da outra aula utilizando getter e setter como o professor fez
class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._fabricante = None
        self._motor = None
    
    @property
    def nome_carro(self):
        return self._nome


    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
    
    @property
    def nome_fabricante(self):
        return self._nome
        


class Motor:
    def __init__(self, nome):
        self._nome = nome
        
    @property
    def nome_motor(self):
        return self._nome
        
        
fusca = Carro('Fusca')
Volkswagen = Fabricante('VolksWagen')
motor_1_0 = Motor('1.0') 
fusca.fabricante = Volkswagen
fusca.motor = motor_1_0
print(fusca.nome_carro, fusca.fabricante.nome_fabricante, fusca.motor.nome_motor)

gol = Carro('Gol') 
gol.fabricante = Volkswagen
gol.motor = motor_1_0
print(gol.nome_carro, gol.fabricante.nome_fabricante, gol.motor.nome_motor)

fiat_uno = Carro('Uno') 
fiat = Fabricante('Fiat') 
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome_carro, fiat_uno.fabricante.nome_fabricante, fiat_uno.motor.nome_motor)

corsa = Carro('Corsa') 
chevrolet = Fabricante('Chevrolet') 
motor_1_6 = Motor('1.6') 
corsa.fabricante = chevrolet
corsa.motor = motor_1_6
print(corsa.nome_carro, corsa.fabricante.nome_fabricante, corsa.motor.nome_motor) 

onix = Carro('Onix') 
onix.fabricante = chevrolet
onix.motor = motor_1_6
print(onix.nome_carro, onix.fabricante.nome_fabricante, onix.motor.nome_motor) 

toro = Carro('Toro')
toro.fabricante = fiat
toro.motor = motor_1_6
print(toro.nome_carro, toro.fabricante.nome_fabricante, toro.motor.nome_motor)
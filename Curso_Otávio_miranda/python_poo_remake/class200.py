# Métodos em instâncias de classes em Python.
class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
        
    def acelerar(self):
        print(self.nome, 'está acelerando...')

carro1 = Carro('Fusca', 'Wolksvagem')
carro2 = Carro('Onix', 'Chevrolet')

print(carro1.nome, carro1.marca)
carro1.acelerar()
print(carro2.nome, carro2.marca)
carro2.acelerar()

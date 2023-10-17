# Métodos em instâncias de classes python
# Hard coded é algo que foi escrito diretamente no código.
class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...') 


carro1 = Carro('Fusca')
print(carro1.nome)
carro1.acelerar()
print()

carro2 = Carro('Corola') 
print(carro2.nome)
carro2.acelerar()
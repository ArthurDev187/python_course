# Métodos em instâncias de classes em Python.
# Classe é um molde, geralmente sem dados.
# Instância da classe (objeto) - Tem dados.
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

carro1 = Carro('Fusca', 'Wolksvagem')
carro2 = Carro('Onix', 'Chevrolet')

print(carro1.nome, carro1.marca)
carro1.acelerar()
Carro.acelerar(carro1)

print(carro2.nome, carro2.marca)
carro2.acelerar()
Carro.acelerar(carro2)

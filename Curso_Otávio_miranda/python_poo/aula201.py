# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
c1 = Carro('Fusca') 
print(c1.nome)
c1.acelerar()

c2 = Carro('Corola') 
print(c2.nome)
c2.acelerar()

c3 = Carro('Celta')
print(c3.nome)
c3.acelerar()

# outra maneira não muito utilizada, mas que funciona também...
Carro.acelerar(c3)
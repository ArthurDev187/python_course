# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        self._cor_tinta = cor
        self._cor_tampa = None
        self._cor_tubo = None
        
    
    @property
    def cor(self):
        print('Estou no property')
        return self._cor_tinta 
    
    @cor.setter
    def cor(self, valor):
        print('Estou no setter')
        self._cor_tinta = valor
    
    
    @property
    def cor_tampa(self):
        print('Estou no property do cor_tampa') 
        return self._cor_tampa 
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('Estou no setter do cor_tampa')
        self._cor_tampa = valor
        
    @property
    def cor_tubo(self):
        print('Estou no property do cor_tubo')
        return self._cor_tubo
    
    @cor_tubo.setter
    def cor_tubo(self, valor):
        print('Estou no setter do cor tubo')
        self._cor_tubo = valor
    
    
    
c1 = Caneta('Azul')
print(c1.cor)
c1.cor = 'Rosa'
print(c1.cor)
print()

c1.cor_tampa = 'roxo'
print(c1.cor_tampa)
c1.cor_tampa = 'Amarelo' 
print(c1.cor_tampa)
print()

c1.cor_tubo = 'Laranja' 
print(c1.cor_tubo) 
c1.cor_tubo = 'Marrom' 
print(c1.cor_tubo)
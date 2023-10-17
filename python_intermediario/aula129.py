from itertools import zip_longest
from copy import deepcopy
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

lista_cidade = zip(l1, l2)
lista_cidade2 = zip_longest(l1, l2, fillvalue='Sem cidade')

lista1 = deepcopy(list(lista_cidade))
lista2 = deepcopy(list(lista_cidade2))
print(lista1) 
print(lista2)
print(lista1) 
print(lista2)
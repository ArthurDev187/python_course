"""
Exiba os indices e itens da lista
"""


lista = ['Arthur', 'Nani', 'Maria', 'Paula', 'Stefani', 'Ana']
# contador = 0
# for i in lista:
#     print(f'indice: {contador}   item: {i} ')
#     contador += 1

indice = range(len(lista))

for i in indice:
    print(i, lista[i])
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1):
    def inner(lista2):
        res = []
        cont = 0
        for i in lista1:
            for n in lista2:
                res.append((i, lista2[cont] ))
                cont += 1
                break
        return res 
    return inner

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

func_lista = zipper(l1)
nova_lista = func_lista(l2)
print(nova_lista)

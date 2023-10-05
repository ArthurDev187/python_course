# considerando duas listas de inteiros ou floats ( lista A e lista B) 
# some os valores nas listas retornando uma nova losta com os valores somados:

# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

# Exemplo:
# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# ============== Resultado
# lista_soma = [2, 4, 6, 8] 

"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = zip(lista_a, lista_b)
lista_somada = []
for i, n in lista_soma:
    lista_somada.append(i + n)
    
print(lista_somada)
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

intervalo = min(len(lista_a), len(lista_b))

lista_somada = []
for i in range(intervalo):
    lista_somada.append(lista_a[i] + lista_b[i]) 

print(lista_somada)

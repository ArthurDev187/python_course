# List comprehension em Python
# List comprehension é uma forma rápida de criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for i in range(10):
    lista.append(i) 
# print(lista)
# print()

lista2 = [f'{i} impar' if i%2==1 else f'{i} par' for i in range(101)] 
# print(lista2)
# print() 

lista3 = [i for i in range(0, 20, 2)]

print(lista3)
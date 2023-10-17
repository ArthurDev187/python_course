# Genarator expression
import sys
lista = [i for i in range(1000000)]
generator = (i for i in range(10000))


print(f'Tamanho lista: {sys.getsizeof(lista)}')
print(f'Tamanho generator: {sys.getsizeof(generator)}')

for i in generator:
    print(i)
    
print(f'Tamanho generator: {sys.getsizeof(generator)}')
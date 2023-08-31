# isinstace - para saber se objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'},]

for item in lista:
    if isinstance(item, set):
        print(f'{item} é um set.') 
    elif isinstance(item, dict):
        print(f'{item} é um dicionário.') 
    elif isinstance(item, tuple):
        print(f'{item} é uma tupla.')
    elif isinstance(item, bool):
        print(f'{item} é um bool.')
    elif isinstance(item, str):
        print(f'{item} é uma string.')
    else:
        print(f'{item} é uma outra coisa.')
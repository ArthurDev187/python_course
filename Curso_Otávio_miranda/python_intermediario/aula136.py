def print_iter(iterador):
    print(*iterador, sep='\n')
    
def filtra_preco(produto):
    return produto['preco'] > 50


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    p for p in produtos if p['preco'] > 50
]

print_iter(novos_produtos)
print() 

outros_produtos = list(filter(
    lambda p: p['preco'] > 50,
    produtos
))

print_iter(outros_produtos)
print()

mais_produtos = list(filter(
    filtra_preco,
    produtos
))

print_iter(mais_produtos)
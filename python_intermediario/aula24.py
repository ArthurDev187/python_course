# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

# nome = 'Arthur'
# print(nome[2])
# print(nome[-2])
# print('A' in nome)
# print('thu' in nome)
# print('turo' in nome)
# print('turo' not in nome)

nome = input('Digite seu nome: ') or 'Você não digitou nada.'
encontrar = input('Digite o que deseja encontrar: ') or 'Se não quer fazer nada então xau.'

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    
# Iterando em strings com while

nome = input('Digite seu nome: ')
contador = 0
novo_nome = ''
while contador < len(nome):
    novo_nome += nome[contador] + '*'
    contador += 1

print(novo_nome)
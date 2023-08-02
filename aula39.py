# Iterando em strings com while

nome = input('Digite seu nome: ')
contador = 0
novo_nome = ''
while contador < len(nome):
    novo_nome += f'*{nome[contador]}'
    contador += 1

novo_nome += '*'
print(novo_nome)
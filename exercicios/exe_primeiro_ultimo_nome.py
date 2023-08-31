# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes
nome_completo = input('Digite o seu nome completo: ') 

primeiro_nome = nome_completo[:nome_completo.find(' ')]
ultimo_nome = nome_completo[nome_completo.rfind(' ')+1:]
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')
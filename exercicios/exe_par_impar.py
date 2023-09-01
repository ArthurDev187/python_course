# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar

while True:
    num = input('Digite um número inteiro: ') 
    try:
        num = int(num) 
    except:
        print('Você não digitou um número inteiro não é mesmo?') 
        continue
    
    if num % 2 == 0:
        print('O número é par.') 
    else:
        print('O número é impar')
    while True:
        opcao = input('Você deseja continuar(S/N)? ').upper().strip()
        if len(opcao) > 1 or len(opcao) < 1:
            print('Digite um caractere.')
            continue
        if 'S' not in opcao and 'N' not in opcao:
            print('Digite apenas S para sim ou N para não.')
            continue
        break

    if opcao == 'S':
        print('Vamos de novo então') 
        print()
        continue
    print('Saindo aqui')
    break
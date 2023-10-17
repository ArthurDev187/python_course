"""
Faça um programa que seja uma lista de compras. O usuário deve ter a possibilidade de inserir, 
apagar e listar valores da sua lista. Não permita que o programa quebre com erros de indices inexistentes na lista.
"""
import os
from time import sleep
lista = []
opcao = ''
opcao_apagar_int = 0
opcao_apagar = ''
print('LISTA DE COMPRAS')
print()
while True:
    
    opcao = input('\nVocê quer (i)nserir, (a)pagar ou (l)istar? ').strip().lower()
    print()
    if len(opcao) > 1:
        print('Digite apenas uma letra para a opcao.')
        sleep(3)
        os.system('cls')
        continue
    
    if opcao == 'i':
        item_a_inserir = input('Digite aqui o item que deseja inserir: ') 
        lista.append(item_a_inserir)
        sleep(1)
        os.system('cls')
    
    elif opcao == 'a':
        print()
        print('=' * 30)
        for indice, item in enumerate(lista):
            print(indice, item)
        print('=' * 30)
        print()
        while True:
            opcao_apagar = input('Digite aqui o número do indice que deseja apagar: ')
            try:
                opcao_apagar_int = int(opcao_apagar) 
            except:
                print('Você não digitou um número para que eu pudesse apagar.')
                sleep(3)
                os.system('cls')
                continue
            
            
            try:
                lista.pop(opcao_apagar_int)
                os.system('cls')
                break
            except:
                print('Você digitou um indice fora do range da lista.')
                sleep(3)
                os.system('cls')
                continue
        
    elif opcao == 'l':
        print()
        print('=' * 30)
        for indice, item in enumerate(lista):
            print(indice, item)
        print('=' * 30)
        print()
            
    else:
        print('Você não digitou nenhuma opção esperada.')
        sleep(3)
        os.system('cls')
        continue
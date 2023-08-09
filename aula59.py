"""
Faça um programa que seja uma lista de compras. O usuário deve ter a possibilidade de inserir, 
apagar e listar valores da sua lista. Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

lista = []
opcao = ''
opcao_apagar_int = 0
opcao_apagar = ''
while True:
    opcao = input('Você quer (i)nserir, (a)pagar ou (l)istar? ') 
    
    if opcao == 'i':
        item_a_inserir = input('Digite aqui o item que deseja inserir: ') 
        lista.append(item_a_inserir)
    
    elif opcao == 'a':
        for indice, item in enumerate(lista):
            print(indice, item)
            
        print()
        while True:
            opcao_apagar = input('Digite aqui o número do indice que deseja apagar: ') 
            try:
                opcao_apagar_int = int(opcao_apagar) 
            except:
                print('Você não digitou um número para que eu pudesse apagar.') 
                continue
            
            
            try:
                lista.pop(opcao_apagar_int)
                break
            except:
                print('Você digitou um indice fora do range da lista.')
                continue
        
    elif opcao == 'l':
        for indice, item in enumerate(lista):
            print(indice, item)

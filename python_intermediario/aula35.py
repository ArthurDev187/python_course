# Repetições 
# while (enquanto)
# Executa uma ação enquanto uma condição for verdadeira

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    if nome == 'sair':
        print('Você saiu')
        break
    print(f'Seu nome é: {nome}') 

print('Acabou')
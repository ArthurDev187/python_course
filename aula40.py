# calculadora com while. Vamos solicitar dois números e um operador, 
# vamos fazer o cálculo logo em seguida e perguntar se quer fazer outro cálculo.
n1 = 0
n2 = 0
op = ''
resultado = 0
opcao = ''

while True:
    
    n1 = int(input('Digite um número inteiro: ')) 
    n2 = int(input('Digite outro número inteiro: ')) 
    op = input('Digite agora um operador: ')
    resultado = 0

    if op == '-':
        resultado = n1 - n2
    elif op == '+':
        resultado = n1 + n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    else:
        print('Digite algum operador entre: "- + * /"')

    print(f'O resultado é: {n1}{op}{n2}= {resultado}')

    opcao = input('Quer fazer outro cálculo? (S/N) ').upper().strip()
    
    if opcao == 'N':
        break
    else:
        ...

print('Saiu do laço.')
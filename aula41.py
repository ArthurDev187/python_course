# calculadora com while melhorada

while True:
    num1 = input('Digite aqui o primeiro número: ')
    num2 = input('Digite aqui o segundo número: ')
    operador = input('Digite aqui um operador entre esses: (+-*/) ')
    valida_num = True
    operador_valido = '+-*/'
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
    except:
        valida_num = False
        
    if valida_num == False:
        print('Um ou ambos os número não são válidos e não foi possível fazer o cálculo.')
        continue
        
    if operador not in operador_valido:
        print('Você não digitou um operador válido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    if operador == '+':
        print(f'{num1}+{num2}= {num1+num2}')
    elif operador == '-':
        print(f'{num1}-{num2}= {num1-num2}')
    elif operador == '*':
        print(f'{num1}*{num2}= {num1*num2}')
    elif operador == '/':
        print(f'{num1}/{num2}= {num1/num2}')
    else:
        print('O programa não deveria chegar aqui.')
        
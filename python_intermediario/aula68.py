"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
print('Vamos agora mostrar se o último número do CPF é válido!!!\n')
cpf = '232.824.890-70'

cpf_formatado = cpf[:13].replace('.', '').replace('-', '')
# print(f'{cpf_formatado=}')

contador = 0
soma = 0
for digit in range(11, 1, -1):
    soma += digit * int(cpf_formatado[contador])
    contador += 1
    
multiplica1 = soma * 10
resto = multiplica1 % 11
digito_final = resto if resto <= 9 else 0 

if int(cpf[13]) == digito_final:
    print(f'O CPF é válido! Número gerado: {digito_final}, CPF: {cpf}\n')
else:
    print(f'O CPF NÃO é válido! Número gerado: {digito_final}, CPF: {cpf}\n')
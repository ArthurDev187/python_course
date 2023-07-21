"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Eu vou dobrar o número que você digitar: ')

try:
    print(f'Número Str: {numero}')
    numero_float = float(numero)
    print(f'Número float: {numero_float:.1f}')
    print(f'O dobro do número que você digitou é: {numero_float*2:.1f}')
except:
    print('Você não digitou um número.')

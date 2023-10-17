# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variável e mostre o valor 
# da variável.


def multiplica_valores(*args):
    valor_final = 1
    for i in args:
        valor_final *= i
        
    return valor_final


numeros_multiplicados = multiplica_valores(1,2,5,4,8,4,5,4,2)

print(numeros_multiplicados)

print(1*2*5*4*8*4*5*4*2)
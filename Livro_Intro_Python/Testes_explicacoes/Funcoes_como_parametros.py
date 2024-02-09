# Aqui podemos ver como podemos passar funções como parâmetros no Python
def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b

def imprime(foper, a, b):
    print(foper(a, b)) 
    return

imprime(soma, 2, 4) 
imprime(subtracao, 10, 6)
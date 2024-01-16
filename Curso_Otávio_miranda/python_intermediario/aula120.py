# Exercício - Adiando execução de funções
def soma(x):
    def soma2(y):
        return x + y
    return soma2

def multiplica(x):
    def mult(y):
        return x * y 
    return mult

def criar_funcao(funcao, *args):
    return funcao(*args) 

soma_com_cinco = criar_funcao(soma, 5) 
soma_final = soma_com_cinco(11)
print(soma_final)

multiplica_por_dez = criar_funcao(multiplica, 10)
multiplica_final = multiplica_por_dez(5)
print(multiplica_final)

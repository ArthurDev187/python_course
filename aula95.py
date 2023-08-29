def executa(funcao, *args):
    return funcao(*args) 

def soma(x, y):
    return x + y 

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero 
    return multiplica

#duplica = cria_multiplicador(2) 

triplica = executa(lambda m: lambda n: m * n, 3)
print(triplica(5))
print() 

variavel = executa(lambda x, y: x + y, 2, 6)
print(variavel)

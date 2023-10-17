# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora')
        
        def aninhada(*args, **kwargs):
            print(f'Parametros do decorador: {a}, {b}, {c}')
            print('Aninhada')        
            result = func(*args, **kwargs)
            return result
        
        return aninhada
    return fabrica_de_funcoes 



@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
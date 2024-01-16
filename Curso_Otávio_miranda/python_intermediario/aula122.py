# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções 
# Decoradores são utilizados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(func):
    def intern(*args):
        for arg in args:
            is_string(arg) 
        result = func(*args)
        return result
    return intern

def invert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param dever ser uma string')


function_invert_string = create_function(invert_string)
inverted_string = function_invert_string('123456')
print(inverted_string)
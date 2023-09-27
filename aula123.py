# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)


def create_function(function):
    def intern(*args, **kwargs):
        for i in args:
            is_string(i) 
            result = function(*args)
        return result
    return intern

@create_function
def invert_string(string):
    print(invert_string.__name__)
    return string[::-1]

def is_string(msg):
    if not isinstance(msg, str):
        raise TypeError('O parâmetro tem que ser string.')


inverted_string = invert_string('12345')
print(inverted_string)

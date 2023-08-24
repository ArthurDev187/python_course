# Higuer order functions
# Funções de primeira classe

def saudacao(msg, nome, *args):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

valor = executa(saudacao, 'Bom dia', 'Arthur', 'Silva', 'ameixa') 

print(valor)
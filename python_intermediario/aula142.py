# Problema dos parametros mutáveis em funções python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
    
lista_1 = adiciona_clientes('Arthur') 
adiciona_clientes('Raquel', lista_1)
print(lista_1)

lista_2 = adiciona_clientes('Pedro') 
adiciona_clientes('Ricardo', lista_2)
print(lista_2)
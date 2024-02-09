# Aqui vamos criar várias funções que configuram o comportamento de uma função final

def imprime_lista(l, fimpressao, fcondicao):
    for e in l:
        if fcondicao(e):
            fimpressao(e) 

def imprime_elemento(e):
    print(f'Valor: {e}') 

def e_par(x):
    return x % 2 == 0

def e_impar(x):
    return not e_par(x) 


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
imprime_lista(lista, imprime_elemento, e_par)
print('*' * 8)
imprime_lista(lista, imprime_elemento, e_impar)
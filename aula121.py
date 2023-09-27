# Variáveis livres + nonlocal

# def fora(x):
#     a = x
#     def dentro():
#         return a * 2
#     return dentro 


# chama_dentro = fora(10) 
# chama_dentro2 = fora(20) 
# chama_dentro3 = fora(30) 

# print(chama_dentro())
# print(chama_dentro2())
# print(chama_dentro3())

def concatenar(string_inicial):
    valor = string_inicial
    
    def interno(valor_a_concatenar=''):
        nonlocal valor
        valor += valor_a_concatenar
        return valor
    return interno

concatena = concatenar('a') 
concatena('b')
concatena('c')
concatena('d')
final = concatena()
print(final)
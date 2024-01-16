# Exercício
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

# def duplica(num1):
#     def triplica(num2):
#         def quadruplica(num3):
#             return f'{num1} duplicado: {num1*2};\n{num2} triplicado: {num2*3};\n{num3} quadruplicado: {num3*4}'
#         return quadruplica
#     return triplica

# variavel = duplica(2)
# variavel = variavel(5) 
# print(variavel(10))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2) 
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2)) 
print(triplicar(2)) 
print(quadruplicar(2))
# Calculo do primeiro dígito do CPF
# CPF: 746.824.890-70

cpf = input('Digite aqui o CPF: ')

digitos_cpf = cpf[:11].replace('.', '')

somador = 0
contador = 0
for i in range(10, 1, -1):
    somador += (i * int(digitos_cpf[contador]))
    contador += 1
    
resultado_somador = somador * 10
resultado_final = resultado_somador % 11
if resultado_final > 9:
    resultado_final = 0


if resultado_final == int(cpf[-2]):
    print(f'O CPF é valido, cpf: {cpf}, dígito do cálculo: {resultado_final}')
else:
    print(f'O CPF NÃO é valido, cpf: {cpf}, dígito do cálculo: {resultado_final}')



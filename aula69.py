from random import randint
#42534098810
cpf = ''
for i in range(9):
    cpf += str(randint(0, 9))


soma_numeros = 0
contagem_regressiva = 10
for numero in cpf:
    soma_numeros += int(numero) * contagem_regressiva
    contagem_regressiva -= 1
    
conta_final = (soma_numeros * 10) % 11 

digito_final = conta_final if conta_final <= 9 else 0

cpf_com_digito = cpf + str(digito_final)
    

cpf_com_digito_valido = cpf + str(digito_final)
soma_numeros = 0
contagem_regressiva = 11
for numero in cpf_com_digito_valido:
    soma_numeros += int(numero) * contagem_regressiva
    contagem_regressiva -= 1
    
conta_final = (soma_numeros * 10) % 11

ultimo_digito = conta_final if  conta_final <= 9 else 0

cpf_final = cpf_com_digito_valido + str(ultimo_digito)


print()
print(f'CPF: {cpf_final}')
# Crie uma função que retorne se o número é par ou impar

def par_impar(num):
    if num % 2 == 0:
        return 'O número é par'
    return 'O número é impar'
    
e_impar_ou_par = par_impar(64533)

print(e_impar_ou_par)
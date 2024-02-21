# Programa que calcula o valor de aumento de salário
print('Cálculo de aumento de salário\n')

salario = float(input('Digite o salário: ')) 
porcentagem = int(input('Digite a porcentagem de aumento: ')) 

porcentagem_aumento = porcentagem / 100 * salario 
print()
print(f'''O salário é de R${salario:.2f} e a porcentagem de aumento foi de {porcentagem}%,
sendo assim o aumento vai ser de R${porcentagem_aumento:.2f} e o salário passará a ser de R${salario + porcentagem_aumento:.2f}.''')
# Programa que calcula o percentual de desconto de uma mercadoria.
print('CALCULA DESCONTO\n') 

valor_mercadoria = float(input('Digite o valor da mercadoria: ')) 
porcentagem_desconto = int(input('Digite o valor da porcentagem de desconto: ')) 

valor_desconto = porcentagem_desconto / 100 * valor_mercadoria

print(f'''O valor da mercadoria era de R${valor_mercadoria:.2f}, a porcentagem de desconto foi de {porcentagem_desconto}%,
sendo assim o desconto foi de R${valor_desconto:.2f} e a mercadoria passa a custar R${valor_mercadoria - valor_desconto:.2f}''')
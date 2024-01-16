# while/else
valor = 'Valorqualquer'
i = 0

while i < len(valor):
    letra = valor[i]
    
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:
    print('O else foi executado.') 

print('Fora do while')
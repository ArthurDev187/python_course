contador = 0

while contador <= 100:
    contador += 1
    
    if contador > 7 and contador < 20:
        print(f'Não vou mostrar o {contador}.')
        continue
    
    if contador == 40:
        print(contador)
        print('Parei por aqui.')
        break
    
    
    print(contador)
    
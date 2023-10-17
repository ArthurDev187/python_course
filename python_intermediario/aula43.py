# Qual letra apareceu mais vezes?
while True:
    frase = input('Digite uma frase: ')
    frase = frase.upper().replace(' ', '')
    letra = ''
    conta_letra = 0
    ultima_contagem = 0
    ultima_letra = ''
    contador_indice = 0
    while contador_indice < len(frase):
        
        letra = frase[contador_indice]

        conta_letra = frase.count(letra)
        if conta_letra > ultima_contagem:
            ultima_contagem = conta_letra
            ultima_letra = letra
        contador_indice += 1
    else:
        print('Acabou a frase.')

    print(f'A letra que mais apareceu na frase foi a letra: "{ultima_letra}"'\
        f' Ela apareceu {ultima_contagem} vezes.')
    print()
    opcao = input('Quer fazer mais uma frase? (S/N)').upper()
    
    if opcao[0] == 'S':
        continue
    else:
        break
print()
print('Acabou o laço.')
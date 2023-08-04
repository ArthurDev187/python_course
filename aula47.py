"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
while True:
    import random
    
    print('Vamos jogar um jogo de adivinhar palavras?\n'
          'Eu vou escolher uma palavra e você tenta adivinhar.\n'
          'Bora começar!\n\n')
    


    lista_palavras = ['BORBOLETA', 'MANGA', 'CHICLETE', 'AMEIXA', 'TELEVISAO', 'ARMARIO', 'ARVORE', 'ESQUINA', 'PARALELEPIPEDO', 'PASSARO']

    palavra = random.choice(lista_palavras)
    palavra_secreta = []
    print('=-' * 40)
    print()
    for letra in palavra:
        palavra_secreta.append('*')

    opcao = ''
    while '*' in palavra_secreta:
        print()
        print(palavra_secreta)
        print()
        opcao = input('Digite uma letra: ').upper().strip()
        if len(opcao) > 1:
            print('Digite apenas uma letra.')
            continue
        contador = 0
        temos = False
        for i in palavra:
            if opcao == i:
                temos = True
                palavra_secreta[contador] = i
                contador += 1
            else:
                contador += 1
        else:
            if temos:
                print(f'\nTemos a letra: {opcao}\n')
            else: 
                print(f'\nNão temos a letra {opcao}\n')
        

    palavra_final = ''
    for i in palavra_secreta:
        palavra_final += i
    
    print('=-' * 40)
    print()
    print(f'Você mandou bem, a palavra era: {palavra_final}')
    print()
    print('=-' * 40)
    print('\n\n')
    jogar_denovo = input('Quer jogar de novo? (S/N) \n').upper().strip()
    
    if jogar_denovo[0] == 'S':
        continue
    else:
        break
print('Acabou o jogo')

# Irei fazer aqui um programa de jogo da forca.
import random

def seleciona_palavra(lista_palavras=[]):
    return random.choice(lista_palavras)

def esconde_palavra(palavra):
    letras_palavra = [] 
    for i in palavra:
        letras_palavra.append('*')
    return letras_palavra

def revela_letras(letra, palavra, palavra_escondida):
    for indice, valor in enumerate(palavra):
        if valor == letra:
            palavra_escondida[indice] = letra 
    return palavra_escondida

def compara_palavras(palavra, palavra_escondida):
    hide_word = ''.join(palavra_escondida)
    if palavra == hide_word:
        return True
    else:
        return False
    


lista_palavras = ['ARMARIO', 'FAZENDA', 'ANIMAL', 'CARRO', 'BICICLETA', 'PARALELEPIPEDO', 'TELEVISAO']

palavra = seleciona_palavra(lista_palavras)
palavra_escondida = esconde_palavra(palavra)
resultado = False
while resultado == False:
    opcao = input('Opção: ').strip().upper()
    revelando_palavra = revela_letras(opcao, palavra, palavra_escondida)
    print(f'{revelando_palavra=}')
    resultado = compara_palavras(palavra, revelando_palavra)

print('Acabou!')
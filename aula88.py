# Exercícios - Sistema de perguntas e respostas
from time import sleep
import emoji
import os

perguntas_respostas = [
    {
        'pergunta' : 'Quem decretou a emancipação da escravidão americara? ',
        'opções' : ['Richard Nixon', 'Benjamin Harrison', 'Abraham Lincoln', 'Jimmy Carter'] ,
        'resposta' : 'Abraham Lincoln'
    },
    {
        'pergunta' : 'Quem inventou o avião? ',
        'opções' : ['Leonardo da Vinci', 'Irmãos Wright', 'Santos Dumont', 'Baianinho de Mauá'] ,
        'resposta' : 'Irmãos Wright'
    },
    {
        'pergunta' : 'Quando foi lançado o primeiro satélite no espaço? ',
        'opções' : ['1957', '1955', '1960', '1962'] ,
        'resposta' : '1957'
    },
    {
        'pergunta' : 'Qual foi o presidente americano que ordenou a explosão das bombas iroxima e nagasaqui?',
        'opções' : ['George W. Bush', 'Harry Truman', 'Richard Nixon', 'Ronald Reagan'] ,
        'resposta' : 'Harry Truman'
    },
    {
        'pergunta' : 'Qual foi a maior descoberta de albert einstein?',
        'opções' : ['O Buraco negro', 'Teoria da relatividade geral', 'Teoria da expansão do universo', 'Teoria dos multiversos'] ,
        'resposta' : 'Teoria da relatividade geral'
    }
]

contador_pontos = 0

for dicionario in perguntas_respostas:
    for chave in dicionario:
        
        if chave == 'pergunta':
            print(f'Pergunta: {dicionario[chave]}\n')
            sleep(3)
        if chave == 'opções':
            for indice, item in enumerate(dicionario["opções"]):
                print(f'Opção {indice+1}: {item}')
            resposta_jogador = int(input('\nDigite a opção da sua resposta: '))
            print()
            sleep(1)
            
            if dicionario["opções"][resposta_jogador-1] == dicionario["resposta"]:
                print(emoji.emojize('Certa resposta!!! :1st_place_medal::red_heart:\n'))
                contador_pontos += 1
            else:
                print(emoji.emojize('Errou!! :sad_but_relieved_face:\n'))
                print(f'A resposta certa é: {dicionario["resposta"]}')
        sleep(2)
    print('='*20)

print(f'Você acertou {contador_pontos} de {len(perguntas_respostas)}')
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
#Agora vou fazer um exercício com esse código que é salvar a listar de tarefas em formator json
import json
import os

lista_tarefas = [] 

opcoes = 'listar desfazer refazer clear salvar'
desfazendo = ''
refazendo = ''
lista_desfeita = []

while True:
    print()
    print('Lista de tarefas. Ações: listar, desfazer e refazer.')
    opcao_usuario = input('Digite uma tarefa ou ação: ').strip().lower()
    if opcao_usuario in opcoes:
        if opcao_usuario == 'listar':
            print()
            print('=' * 20)
            print(*lista_tarefas, sep='\n')
            print('=' * 20)
            print()
            
            
            
        elif opcao_usuario == 'desfazer':
            if len(lista_tarefas) == 0:
                print()
                print('Não tem conteúdo nenhum na lista para ser desfeito.')
                print()
                continue
            desfazendo = lista_tarefas.pop()
            lista_desfeita.append(desfazendo)
            
            
        elif opcao_usuario == 'refazer':
            if desfazendo == '':
                print()
                print('Você não desfez nada para poder refazer.')
                print()
                continue
            elif len(lista_desfeita) == 0:
                print()
                print('Não tem mais conteúdo para refazer.')
                print()
                continue
            refazendo = lista_desfeita.pop()
            lista_tarefas.append(refazendo)
        
        elif opcao_usuario == 'clear':
            os.system('clear')
        
        elif opcao_usuario == 'salvar':
            print('Por favor, digite o nome do arquivo ou o caminho para que sua lista de tarefas possa ser salva.')
            nome_caminho = input('Digite aqui: ')
            with open(nome_caminho+'.json', 'w', encoding='utf8') as arquivo:
                json.dump(
                    lista_tarefas,
                    arquivo,
                    ensure_ascii=False,
                    indent=2
                )
            
        continue
            
    lista_tarefas.append(opcao_usuario)
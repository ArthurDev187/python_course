"""
Repeições com while 
laçõs aninhados
"""
tamanho_linha = 5
tamanho_coluna = 5

linha = 0
coluna = 0



while coluna <= tamanho_coluna:
    linha = 0
    coluna += 1
    print(f'{coluna=}')
    while linha <= tamanho_linha:
        linha += 1
        print(f'{linha=}')

    
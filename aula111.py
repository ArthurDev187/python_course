# try, except, else e finally

try:
    print('Abrir arquivo')
    2/0
except ZeroDivisionError as e:
    print(e)
else:
    print('Não teve erro')
finally:
    print('Fechar arquivo')
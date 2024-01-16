# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('Abrir arquivo')
    2/0
except ZeroDivisionError as e:
    print(e)
else:
    print('Não teve erro')
finally:
    print('Fechar arquivo')
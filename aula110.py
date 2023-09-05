# try, except


try:
    a = 12
    b = 2
    c = a / b
    print(c)
except ZeroDivisionError:
    print('Erro divisão por zero.')
except NameError:
    print('variável a ou b não definidas.')
except TypeError:
    print('Type Error')


    
    
    
# try, except


try:
    # print('Linha1'[1000])
    a = 12
    b = 2
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError as e:
    print(e.__class__.__name__)
    print(e)
except IndexError as e:
    print(e.__class__.__name__)
    print(e)
except TypeError as e:
    print(e.__class__.__name__)
    print(e)


    
    
    
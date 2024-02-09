# programa com a função recursiva modiificada para facilitar o rastreamento.

def fatorial(n):
    if n in (0, 1):
        return 1
    else:
        fat = n * fatorial(n - 1) 
    return fat

num = 4
fatresult = fatorial(num)
print(f'Fatorial de {num} = {fatresult}')
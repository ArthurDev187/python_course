# Uma função recursiva é uma função que chama a sí mesma.
def fatorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * fatorial(n - 1) 

a = fatorial(4) 
print(a)
# def generator(n=0):
    
#     yield 1 #pausa a execução
#     print('Vamos continuar...') 
    
#     yield 2 #pausa novamente
#     print('Continuando...')
    
#     yield 3 #pausa 
#     print('Mais uma vez...') 
    
#     yield 4 * 2
#     print('Vou acabar por aqui.') 
    
#     return 10

# gen = generator(0)

# for i in gen:
#     print(i)
    
    
def generator(inicio=0, fim=10):
    while True:
        yield inicio
        inicio += 1
        
        if inicio >= fim:
            return
        
        
        
gen = generator(inicio=0, fim=20) 

for i in gen:
    print(i)
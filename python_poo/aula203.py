# Mantendo estado dentro das classes

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return
        
        print(f'{self.nome} está iniciando a filmagem...')
        self.filmando = True
        
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} filmando... não é possível fotografar.')
            return
        
        print(f'{self.nome} fotografou.') 
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...') 
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
        



c1 = Camera('Canon') 

c1.parar_filmar()
c1.filmar()
c1.filmar()
print(c1.filmando)
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.parar_filmar()

print()
print()

c2 = Camera('Canon') 

print(c2.filmando)
c2.fotografar()
c2.filmar()
c2.fotografar()
print(c2.filmando)
c2.parar_filmar()
c2.filmar()
c2.parar_filmar()
c2.parar_filmar()

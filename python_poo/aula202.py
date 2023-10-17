# Escopo da classe e de métodos da classe
class Animal:
    
    def __init__(self, especie):
        self.especie = especie
        
        self.variavel = 'Valor' 
        print(self.variavel) 
        
    def executa(self):
        return self.variavel
    
    def comendo(self, alimento):
        return f'{self.especie} está comendo {alimento}'
        

animal_1 = Animal(especie='Leão')
animal_1.executa() 

animal_2 = Animal(especie='Tigre')

animal_3 = Animal(especie='Coala') 
coala_comendo = animal_3.comendo('Pêra')

print()
print(coala_comendo)
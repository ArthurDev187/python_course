# Aprendendo um pouco sobre arquivos em python, como trabalhar com eles.

with open('numeros.txt', 'a+') as arquivo:
    for i in range(1, 101): 
        arquivo.write(f'{i}\n') 
 
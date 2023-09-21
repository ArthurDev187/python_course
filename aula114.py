# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys
import aula114_m
from aula114_m import soma_dois, variavel_modulo
#sys.path.append(r'C:\Users\silva\OneDrive\Documentos\Curso_python_3\python_course\exercicios')
print(aula114_m.variavel_modulo)

soma = aula114_m.soma_dois(2, 7)
print(soma)
print()

print(variavel_modulo) 
print(soma_dois(7, 7))

# caminhos = sys.path

# print(*caminhos, sep='\n')
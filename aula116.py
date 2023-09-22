from aula116_package import mod 
from aula116_package.mod import soma_dois
import aula116_package


soma = mod.soma_dois(2, 3) 
print(soma)

soma2 = aula116_package.mod.soma_dois(1, 2) 
print(soma2)

soma3 = soma_dois(10, 20) 
print(soma3)
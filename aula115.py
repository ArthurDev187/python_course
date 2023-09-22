import importlib

import aula115_m

print(aula115_m.variavel)

for i in range(10):
    importlib.reload(aula115_m)
    print(i)

print('Fim')
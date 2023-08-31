# Genarator expression, Iteraveis e iterator em Python

iteravel = ['Eu', 'tenho', 'um', 'Iterator'] 
iterator = iter(iteravel) 

print(next(iterator))
print(next(iterator))
# print(next(iterator))
# print(next(iterator))
print("-"*15)
print('Acabou o print iterator next')
print("-"*15)
for i in iterator:
    print(i)
print()
# print(next(iterator))
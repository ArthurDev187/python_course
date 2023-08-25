# testando os dicionários

data = {
    'Nome' : 'Arthur',
    'sobrenome' : 'Rodrigues',
    'idade' : int('28'), 
    'Ano nascimento' : '1995',
    'Peso' : float('100'),
    'altura' : '1.73',
    'telefone' : ('11 98806-0409', '11 96856-7079'),
    'endereco' : {
        'Rua' : 'Tore albert Munk',
        'N°' : '445',
        'Bairro' : 'Jardim Leonor',
        'Cidade' : 'Cotia',
        'Estado' : 'São Paulo',
        'CEP' : '06700-149'
            },
    'skills' : [
        'Python',
        'AWS',
        'HTML',
        'CSS',
        'SQL',
        'JAva',
        'JavaScript',
        'MongoDB',
        'Django'
    ]
}


for key in data:
    print(f'{key}: {data[key]}')
print()

for i in data['telefone']:
    print(f'Telefone: {i}')
print()

for i in data['endereco']:
    print(f'{i}: {data["endereco"][i]}')    
print()

print('Skills: ')
for i in data['skills']:
    print(i) 
    
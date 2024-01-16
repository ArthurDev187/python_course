def mostra_args(*args, **kwargs): 

    for key, value in kwargs.items():
        print(key, value) 
        

pessoa1 = {
    'nome' : 'Arthur',
    'sobrenome' : 'Rodrigues',
    'idade' : '28',
    'nacionalidade' : 'Brasileiro'
}

endereco1 = {
    'rua' : 'Tore Albert Munk',
    'n°' : '445',
    'bairro' : 'Jardim Leonor',
    'cidade' : 'Cotia',
    'estado' : 'SP',
    'cep' : '06700-149'
}

dados_pessoa1 = {**pessoa1, **endereco1} 

mostra_args(1,2,3)
mostra_args(**dados_pessoa1)
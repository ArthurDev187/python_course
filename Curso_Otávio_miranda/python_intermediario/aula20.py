primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor: {primeiro_valor} é o maior.')
elif segundo_valor > primeiro_valor:
    print(f'Segundo valor: {segundo_valor} é maior.')
else:
    print('Os valores são iguais.')
    
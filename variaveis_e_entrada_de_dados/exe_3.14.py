# Programa que pergunte a quantidade de KM percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
# R$ 60 por dia e R$0,15 por KM rodado.
print('PROGRAMA DE CARRO ALUGADO\n') 

dias_alugado = int(input('Digite aqui a quantidade de dias que o carro foi alugado: ')) 
km_percorrido = int(input('Digite aqui a quantidade de Km percorrido com o veículo: ')) 

valor_dias = dias_alugado * 60.0
valor_km = km_percorrido * 0.15

preco_a_pagar = valor_dias + valor_km

print(f'''\n  O carro foi alugado por {dias_alugado} dias e o valor total pelas diárias foi: R${valor_dias:.2f}
  rodou por {km_percorrido}Km, o valor total dessa quilometragem foi de R${valor_km:.2f}
  O valor total a pagar é: R${preco_a_pagar:.2f}''')

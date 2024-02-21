# Programa que pega o valor de dias, horas, minutos e segundos do usuário e converte tudo para segundos.
print('CONVERTENDO TUDO PARA SEGUNDOS\n') 

dias = int(input('Digite o valor de dias: '))
horas = int(input('Digie o valor de horas: '))
minutos = int(input('Digite o valor de minutos: ')) 
segundos = int(input('Digite o valor de segundos: ')) 

total_dias_em_segundos = ((dias * 24) * 60) * 60
total_horas_em_segundos = (horas * 60) * 60
total_minutos_em_segundos = minutos * 60 
total_em_segundos = total_dias_em_segundos + total_horas_em_segundos + total_minutos_em_segundos + segundos

print()
print(f'O total de dias em segundos é: {total_dias_em_segundos}') 
print(f'O total de horas em segundos é: {total_horas_em_segundos}')
print(f'O total de minutos em segundos é: {total_minutos_em_segundos}') 
print(f'E o total juntando todos em segundos é: {total_em_segundos}')
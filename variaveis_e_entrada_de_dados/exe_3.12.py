# Programa que calcule o tempo de uma viagem de carro, pergunte a distância a percorrer e a velocidade média esperada para a viagem.
print('PROGRAMA QUE CALCULA TEMPO DE VIAGEM DE CARRO\n') 

km_distancia = int(input('Digite a quilometragem que será percorrida na viagem: ')) 
velocidade_media = int(input('Digite a velocidade em KM/h média da viagem: ')) 
print()

tempo_viagem = km_distancia / velocidade_media  
print(tempo_viagem)
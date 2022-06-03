'''
desafio 31
desenvolva um programa que calcule o preço a passagem do onibus
para viagens ate 200km = 0,50 po km mais longo 0,45 por km
'''

#### 031 ####

distancia = float(input('Qual a distância para onde deseja viajar? '))

if distancia <= 200:
  valor = distancia * 0.50
else:
  valor = distancia * 0.45

print('A distância é de {} e o valor é de {}'.format(distancia, valor))
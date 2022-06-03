'''
desafio 15
faça um programa que que pergunte a quantidade de dias e kms de um carro alugado
e calcule o valor do aluguel. dia = 60; km = 0,15
'''

#### 015 ####

dia = int(input('Quantos dias o carro ficou alugado? '))
km = int(input('Quantos Kms foram rodados? '))

day = (dia * 60)
kilom = (km * 0.15)
aluguel = day + kilom 

print('O valor a ser pago é {} reais.'.format(aluguel))
print('Especificação de valor:\n>>> Dias {} * 60 = {} reais.\n>>> Distância {} * 0,15 = {}'.format(dia, day, km, kilom))
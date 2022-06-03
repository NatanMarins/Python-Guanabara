'''
desafio 14
faça um programa que coverta a temperatura de °C para °F e K
'''

#### 014 ####

tempC = float(input('Digite a temperatura em °C: '))

tempF = (tempC * 9 / 5) + 32
tempK = tempC + 273

print('A temperatura de {} °C, corresponde a:\n>>>{} °F\n>>>{} k'.format(tempC, tempF, tempK))
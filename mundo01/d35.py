'''
desafio 35
desenvolva um programa que leia o valor de três retas e diga se elas podem formar um triângulo
'''

#### 035 ####

reta1 = float(input('Informe o valor da reta em m: '))
reta2 = float(input('Informe o valor da reta em m: '))
reta3 = float(input('Informe o valor da reta em m: '))

reta12 = reta1 + reta2
reta13 = reta1 + reta3
reta23 = reta2 + reta3

if reta12 > reta3 and reta13 > reta2 and reta23 > reta1:
  print('As medidas:\n>>> {}m\n>>> {}m\n>>> {}m\nFormam um triângulo'.format(reta1, reta2, reta3))
else:
  print('As medidas:\n>>> {}m\n>>> {}m\n>>> {}m\nNão formam um triângulo'.format(reta1, reta2, reta3))
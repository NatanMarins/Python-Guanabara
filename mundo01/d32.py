'''
desafio 32
fça um programa que descubra se o ano é bissesto
'''

#### 032 ####

ano = int(input('Informe o ano: '))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('{} é bissesto'.format(ano))
else:
  print('{} não é bissesto'.format(ano))
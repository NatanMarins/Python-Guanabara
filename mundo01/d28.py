'''
desafio 28
faça um programa que faça o computador pensar um numero de um ate 5 e o usuario tem que tentar
acetar o numero
'''

#### 028 ####

myNum = int(input('Escolha um número de 0 a 5: '))

import random

gameNum = random.randrange(0, 5)

print('O seu número é {}\nO computador escolheu {}'.format(myNum, gameNum))

if gameNum == myNum:
  print('\033[1;32;45mParabéns! Você venceu :)')
else:
  print('\033[1;31;37mTente Novamente! :(')
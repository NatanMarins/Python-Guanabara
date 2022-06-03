'''
desafio 17
faça um programa que leia o comprimento dos catetos oposto e adjacente e mostro o comprimento da hipotenusa
'''

#### 017 ####

import math
catOp = int(input('Informe o valor do cateto oposto: '))
catAdj = int(input('Informe o valor do cateto adjacente: '))

hipotenusa = math.hypot(catOp, catAdj)

print('O valor da hipotenusa é {}'.format(hipotenusa))
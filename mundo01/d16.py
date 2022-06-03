'''
desafio 16
crie um programa que leia um número real quakquer e mostre sua parte inteira
'''
#### 016 ####

import math
num =  float(input('Digite um valor real: '))

inteiro = num

print('A parte inteira do valor {}, é {}'.format(num, math.trunc(inteiro)))
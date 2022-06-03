'''
desafio 18
faça um programa que leia um angulo e mostre seu seno cosseno e tangente
'''

#### 018 ####
import math
angulo = int(input('Informe o valor do ângulo: '))

print('O seno de {} é: {:.3f} \nO cosseno de {} é: {:.3f} \nA tangente de {} é: {:.3f}'.format(angulo, math.sin(angulo), angulo, math.cos(angulo), angulo, math.tan(angulo)))
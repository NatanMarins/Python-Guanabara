'''
desafio 30
crie um programa pra decobrir se um número é impar ou par
'''

#### 030 ####

import random

num = random.randrange(1,99999)

if (num % 2) == 0:
  print('{} é par'.format(num))
else:
  print('{} é impar'.format(num))
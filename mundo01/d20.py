'''
desafio 20
sortear a ordem de apresentação de trabalhos dos alunos. leia o nome dos quatro alunos e mostre a ordem
'''

#### 020 ####

import random

a1 = str(input('Informe o nome dos alunos: '))
a2 = str(input('Informe o nome dos alunos: '))
a3 = str(input('Informe o nome dos alunos: '))
a4 = str(input('Informe o nome dos alunos: '))

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print('A ordem de apresentação será:\n{}'.format(alunos))
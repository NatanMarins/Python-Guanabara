'''
desafio 19
um porfessor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que leia o nome
deles e escreva o escolhido
'''

#### 019 ####

import random

a1 = str(input('Informe o nome dos alunos: '))
a2 = str(input('Informe o nome dos alunos: '))
a3 = str(input('Informe o nome dos alunos: '))
a4 = str(input('Informe o nome dos alunos: '))

alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)

print('O aluno escolhido é: {}'.format(escolhido))
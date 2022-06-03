'''
desfaio 27
faça um programa que leia o nome completo de uma pessoa que mostre seu primeiro
e último nome
'''

#### 027 ####

nome = str(input('Informe seu nome completo: ')).strip()

vetName = nome.split(' ')
first = vetName[0]
last = vetName[-1]

print('Seu nome é: {} {}'.format(first, last))
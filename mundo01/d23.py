'''
desfaio 23
faça um programa que leia um número e mostre separado
'''

#### 023 ####

num = str(input('Digite um número de 0 até 9999: '))

vetNum = list(num)

print('Unidades de:\n>>>Milhar: {}\n>>>Centena: {}\n>>>Dezena: {}\n>>>Unidade: {}'.format(vetNum[0], vetNum[1], vetNum[2], vetNum[3]))
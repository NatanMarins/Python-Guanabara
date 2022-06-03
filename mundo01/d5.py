'''
desafio 05
 Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e 
 antecessor.
'''

#### 005 ####

n1 = int(input('Digite um valor: '))

ant = n1 - 1
suc = n1 + 1

print('Seu sucessor é {}\nSeu antecessor é {}'.format(suc, ant))
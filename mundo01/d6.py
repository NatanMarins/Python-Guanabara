'''
desafio 6
crie um algoritmo que leia um número e mostre o seu dobro, triplo
e a raiz quadrada.
'''

#### 006 ####

n1 = int(input('Digite um valor: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('O dobro do valor {} é {} \nO triplo é {} \nA raiz quadrada é {}'.format(n1, d, t, r))
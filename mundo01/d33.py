'''
desafio 33
faça um programa que leia três números e mostre o maior e o menor
'''

#### 033 ####

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1 > num2:
  maior = num1
else:
  maior = num2

if maior > num3:
  maior = maior
else:
  maior = num3

if num1 < num2:
  menor = num1
else:
  menor = num2

if menor < num3:
  menor = menor
else:
  menor = num3


print('O maior valor é {} e o menor valor é {}'.format(maior, menor))

# outra forma

valores = []
valores.append(num1)
valores.append(num2)
valores.append(num3)
valores.sort

print('O maior valor é {} e o menor valor é {}'.format(valores[2], valores[0]))
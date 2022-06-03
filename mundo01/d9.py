'''
desafio 9
faça um programa que leia um número inteiro qualquer e mostre sua tabuada 
'''

#### 009 ####

val = int(input('Informe o valor para saber a tabuada: '))
print('Tabuada de {}:'.format(val))
c = 0
while c <= 9:
  tabuada = val * c
  c += 1
  print('{} X {} = {}\n'.format(val, c, tabuada))
'''
desfaio 25
crie um programa que leia o nome de uma pessoa e fale se ela tem silva no nome
'''

#### 025 ####

nome = str(input('Informe seu nome completo: '))

nome = nome.lower()

if 'silva' in nome:
  print('Tem Silva no nome.')
else:
  print('Não tem Silva no nome.')
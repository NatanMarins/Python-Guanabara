'''
desfaio 24
crie um programa que leia o nome de uma cidade e fale se ela começa com santo.
'''

#### 024 ####

city = str(input('Informe o nome da cidade: '))

city = city.lower().split()


if 'santo' in city[0]:
  print('A cidade tem um nome referente a um santo.')
else:
    print('O nome não tem referencia a nenhum santo.')
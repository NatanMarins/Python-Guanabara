'''
desafio 29
escreva um programa que leia a velocidade de um carro se le passar do limite
de 80 km/h recebera multa de 7 reais por km.
'''

#### 029 ####

vel = int(input('Qual foi a sua velocidade: '))

if vel < 80:
  print('Voçê não foi multado :)')
else:
  print('Voçê foi multado :(')
  dif = vel - 80
  preco = dif * 7
  print('Terá que pagar {} reais'.format(preco))
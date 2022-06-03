'''
desafio 11
faça um programa que leia a largura e a altura de uma parede em metros,
calcula a sua área e a quantidade de tinta para pintá-la. tinta = 2m^2
'''

#### 011 ####

h = float(input('Informe a altura da parede em metros: '))
l  = float(input('Informe a largura da parede em metros: '))

area = h * l
tinta = area / 2

print('Sua parede tem {:.2f}m²\nPara pintar toda parede será gasto {:.2f} latas de tinta'. format(area, tinta))
'''
desafio 34
escreva um programa que leia o salário se for maior que 1250 aumento de 10%
se for menor 15%
'''

#### 034 ####

salario = float(input('Informe seu salário: '))

if salario > 1250:
  salario = (salario * 0.10) + salario
else:
  salario = (salario * 0.15) + salario

print('Seu novo salário é de {} reis'.format(salario))
'''
desafio 13
faça um algoritmo que leia o salário de um funcioário e mostre seu
novo salário com 15% de aumento
'''

#### 013 ####

salario = float(input('Informe sua salário: '))

aumento = salario * 0.15
neoSalario = salario + aumento

print('Parabéns!!!!\nSeu novo salário é de {:.2f}\nVoçê teve um aumento de {:.2f} reais'.format(neoSalario, aumento))
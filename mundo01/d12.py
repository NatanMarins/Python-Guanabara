'''
DESAFIO 12
faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto
'''

#### 012 ####

preco = float(input('Informe o valor do produto: '))

desconto = preco * 0.05
neoPreco = preco - desconto

print('Valor pormocional de {:.2f}\nO desconto é de {:.2f} reais'.format(neoPreco, desconto))
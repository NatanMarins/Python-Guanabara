'''
desafio 10
crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar. dol = 3,27 reais
'''

#### 010 ####

money = float(input('Informe o valor para ser convertido: '))

cambio = money / 3.27

print('Cotação de hoje:\nU$ 1,00 = R$ 3,27\nCom {} reais, voçê conseguirá comprar {:.2f} dólares'.format(money, cambio))
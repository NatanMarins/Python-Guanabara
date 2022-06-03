'''
desfaio 26
faça um programa que leia uma frase e mostre quantas vezes aparece a letra a,
em que posição ela aparece pela primeira vez e em que posição ela aparece pela 
última vez
'''

#### 026 ####

frase = str(input('Digite uma frase: ')).lower()

count = frase.count('a')
first = frase.find('a') + 1
last = frase.rfind('a') + 1

print('A frase é: {}\nA quantidade de vezes que a letra A aparece é: {}\nAparece pela primeira vez na posição: {}\nAparece pela última vez na posição: {}'.format(frase, count, first, last))
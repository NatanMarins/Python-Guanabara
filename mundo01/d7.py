'''
deafio 7
desenvolva um programa que leia as duas notas dos alunos, calcule e mostre a sua média.
'''

#### 007 ####
nome = str(input('Informe o nome do aluno: '))
nTeste = float(input('Informe a nota do teste: '))
nProva = float(input('Informe a nota da prova: '))

media = (nTeste + nProva) / 2

print('A média do aluno {} é: {}'.format(nome, media))

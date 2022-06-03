'''
desfaio 22
crie um programa que leia o nome de uma pessoa e o nome todo maiusculo,
minusculo, quantas letras e quantas letras tem o primeiro nome
'''

#### 022 ####

nome = str(input('Informe seu nome completo: ')).strip()

nome_up = nome.upper()
nome_low = nome.lower()
vetName = nome.split()
qtd1nome = len(vetName[0])
nomeJunto = nome.replace(" ", "")
qtdNome = len(nomeJunto)



print(""">>Nome em Maiúsculo: {};\n>>>Nome em minúsculo: {};\n>>>>Quantidade de letras: {};\n>>>>>Quantidade de letras do primeiro nome: {}.""".format(nome_up, nome_low, qtdNome, qtd1nome))
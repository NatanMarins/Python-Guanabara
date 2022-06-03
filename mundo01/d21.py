'''
desafio 21
faça um programa que abra e reproduza o audio de um arquivo mp3
'''

#### 021 ####

import pygame
pygame.init()

pygame.mixer.music.load('''caminho da pasta no computador''')
pygame.mixer.music.play()
pygame.mixer.music.wait

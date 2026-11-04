# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

print('\nEscolha a música a ser reproduzida:\n')
musica = str(input('\nMúsicas disponíveis:\n\nEx021.mp3 --> Life Could Be A Dream\n\nIndique o código da Música: '))

pygame.init() #Iniciando a biblioteca pygame

pygame.mixer.music.load(musica) #Selecionando a Música a ser tocada

pygame.mixer.music.play() #Iniciando a musica

input('\n\nTecle ENTER para terminar a música!')

pygame.event.wait() #Termina a música
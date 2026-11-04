'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

ano = int(input('\nInforme um ano qualquer, verificaremos se o próprio é BISSEXTO.\n\nAno: '))

if (ano % 4) == 0:
    print('\n{} é um ano BISSEXTO.'.format(ano))
else:
    print('\n{} não é um ano BISSEXTO.'.format(ano))
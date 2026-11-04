# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('\nInforme o nome de uma pessoa, o programa verificará se possui "SILVA" no próprio.\n\nNome: '))
print('\nO nome informado contém "SILVA": {}'.format('SILVA' in nome.upper().split()))
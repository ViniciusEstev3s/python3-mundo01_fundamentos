# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('\nInforme o nome de uma cidade, o programa verificará se o primeiro nome é "SANTO".\n\nCidade: '))
print('\nO primeiro nome da cidade contém "SANTO": {}'.format('SANTO' in cidade.upper().split()[0]))
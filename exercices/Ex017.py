# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa

from math import sqrt, hypot

print('\nInforme o comprimento do cateto oposto e cateto adjacente, o programa exibirá, com base nos dados,', end='')
print(' o comprimento da hipotenusa.')
cat_oposto = float(input('\nComprimento do cateto oposto em centímetros: '))
cat_adjacente = float(input('\nComprimento do cateto adjacente em centímetros: '))
hipotenusa = sqrt(pow(cat_oposto, 2) + pow(cat_adjacente, 2))
# hipotenusa = hypot(cat_oposto, cat_adjacente)  | Maneira alternativa de calcular a hipotenusa
print('\nConforme os dados informados, cateto oposto possuindo {:.2f}cm e cateto'.format(cat_oposto), end=' ')
print('adjacente possuindo {:.2f}cm, a hipotenusa resultante foi de {:.2f}cm!.'.format(cat_adjacente, hipotenusa))
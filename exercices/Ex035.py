'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo'''

reta_1 = float(input('\nInforme o comprimento(m) de 3 retas, informaremos se é possível formar um triângulo\n\nReta 1: '))
reta_2 = float(input('\nReta 2: '))
reta_3 = float(input('\nReta 3: '))
if (reta_1 + reta_2) > reta_3 and (reta_2 + reta_3) > reta_1 and (reta_1 + reta_3) > reta_2:
    print('\nÉ possível formar um Triângulo.')
else:
    print('\nNão é possível formar um triângulo.')
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².

print('\nInforme a altura e largura em metros da parede que será pintada, o programa irá calcular o consumo de tinta por m².')
l = float(input('\nLargura: '))
a = float(input('\nAltura: '))
area = l*a
print('\nInformado a metragem de {:.2f}m de largura e {:.2f}m de altura'.format(l, a), end='')
print(', o consumo de tinta para {:.2f}m² será de {:.2f}l de tinta.'.format(area, area/2))

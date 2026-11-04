# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('\nInforme um número inteiro qualquer para que seja exibida a tabuada do próprio.\n\nNúmero inteiro: '))
print('\n1x{}={}\n2x{}={}\n3x{}={}\n4x{}={}\n5x{}={}\n6x{}={}'.format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6), end='')
print('\n7x{}={}\n8x{}={}\n9x{}={}\n10x{}={}'.format(n, n*7, n, n*8, n, n*9, n, n*10))

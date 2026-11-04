# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira

from math import trunc

num = float(input('Informe um número real qualquer, o programa exibirá apenas sua parte inteira: \n\nNúmero Real: '))
print('\nO número informado foi {:.3f}, sua parte inteira é {}!.'.format(num, trunc(num)))

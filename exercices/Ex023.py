''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834;
Unidade: 4;
Dezena: 3;
Centena: 8;
Milhar: 1. '''

num = int(input('\nInforme um número de 0 a 9999, o próprio passará por uma análise de dados.\n\nNúmero:'))
''' 
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
'''
print('\nUnidade: {}'.format(num//1%10))
print('\nDezena: {}'.format(num//10%10))
print('\nCentena: {}'.format(num//100%10))
print('\nMilhar: {}'.format(num//1000%10))
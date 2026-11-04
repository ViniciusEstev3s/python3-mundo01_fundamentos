'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar'''

num = int(input('\nInforme um número inteiro qualquer, identificaremos se o próprio é ímpar ou par.\n\nNúmero: '))
par_impar = num % 2
if par_impar > 0 :
    print('\nO número {} é ímpar!'.format(num))
else:
    print('\nO número {} é par!'.format(num))
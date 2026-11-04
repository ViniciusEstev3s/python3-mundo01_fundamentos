'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num_1 = float(input('\nInforme três números, o programa apontará o menor e o maior.\n\nNúmero 1: '))
num_2 = float(input('\nNúmero 2: '))
num_3 = float(input('\nNúmero 3: '))
if num_1 > num_2 and num_1 > num_3 :
    print('\n{:.2f} é o maior número.'.format(num_1))
else:
    if num_2 > num_1 and num_2 > num_3 :
        print('\n{:.2f} é o maior número.'.format(num_2))
    else:
        if num_3 > num_2 and num_3 > num_1 :
            print('\n{:.2f} é o maior número.'.format(num_3))
if num_1 < num_2 and num_1 < num_3 :
    print('\n{:.2f} é o menor número.'.format(num_1))
else:
    if num_2 < num_1 and num_2 < num_3 :
        print('\n.{:.2f} é o menor número.'.format(num_2))
    else:
        if num_3 < num_2 and num_3 < num_1 :
            print('\n{:.2f} é o menor número.'.format(num_3))
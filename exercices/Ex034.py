'''Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o  aumento é de 15%.'''

renda_func = float(input('\nInforme a renda do funcionário, o próprio receberá um aumento específico.\n\nRenda: R$'))
if renda_func > 1250 :
    renda_func = renda_func + (renda_func * 0.1)
    print('\nSeu salário é superior ao valor de R$1250,00, por isso, você recebeu 10% de aumento.', end='')
    print('\nNovo Salário: {:.2f}.'.format(renda_func))
else:
    renda_func = renda_func + (renda_func * 0.15)
    print('\nSeu salário é inferior ou igual ao valor de R$1250,00, por isso, você recebeu 15% de aumento.', end='')
    print('\nNovo Salário: {:.2f}.'.format(renda_func))
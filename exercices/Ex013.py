# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('\nInforme o salário do funcionário, para que seja acrescentado um aumento de 15% no próprio.\n\nSalário: R$'))
aumento15 = salario + (salario*0.15)
print('\nInformado o salário de R${:.2f}, o próprio passou por aumento de 15%, valendo assim, R${:.2f}!.'.format(salario, aumento15))

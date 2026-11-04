# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

print('\nInforme as notas do aluno para que a média seja calculada.')
n1 = float(input('\nPrimeira nota: '))
n2 = float(input('\nSegunda nota: '))
print('\nA média entre as notas foi de {:.2f}!.'.format((n1+n2)/2))

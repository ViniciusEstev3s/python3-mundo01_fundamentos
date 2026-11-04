# Faça um programa ue leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações pssíveis sobre
# ele.

num = input('\nDigite algo qualquer para que o programa possa analisar sua procedência: ')
print('\n\nO tipo primitivo é:',type(num))
print('\nÉ númerico? {}.'.format(num.isnumeric()))
print('\nÉ alfabético? {}.'.format(num.isalpha()))
print('\nÉ alfanúmerico? {}.'.format(num.isalnum()))
print('\nEstá em caixa alta? {}.'.format(num.isupper()))
print('\nEstá em caixa baixa? {}.'.format(num.islower()))
print('\nEstá capitalizado? {}.'.format(num.istitle()))
print('\nContém apenas espaço? {}.'.format(num.isspace()))

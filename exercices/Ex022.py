''' Crie um programa que leia o nome completo de uma pessoa e mostre:

• O nome com todas as letras maiúsculas.
• O nome com todas as letras minúsculas.
• Quantas letras ao todo(sem considerar espaços).
• Quantas letras tem o primeiro nome. '''

nome = str(input('\nInforme o nome completo de uma pessoa, o próprio passará por uma análise de dados.\n\nNome: '))
print('\n• Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('\n• Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('\n• Número de letras que o nome contém(sem considerar espaços): {}'.format(len(''.join(nome.split()))))
print('\n• Número de letras que o primeiro nome contém: {}'.format(len(nome.split()[0])))
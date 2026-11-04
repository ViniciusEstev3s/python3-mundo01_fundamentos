''' Faça um programa que leia uma frase pelo teclado e mostre:

• Quantas vezes aparece a letra "A".
• Em que posição ela aparece pela primeira vez.
• Em que posição ela aparece pela ultima vez. '''

frase = str(input('\nDigite uma frase, a própria passará por uma analise de dados.\n\nFrase: '))
print('\nQuantas vezes aparece a letra "A": {}'.format(frase.count('A')))
print('\nEm que posição na string o "A" aparece pela primeira vez: {}'.format(frase.find('A')+1))
print('\nEm que posição na string o "A" aparece pela ultima vez: {}'.format(frase.rfind('A')+1))
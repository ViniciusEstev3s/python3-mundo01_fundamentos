''' Um Professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo os nomes e escrevendo o nome do escolhido '''

from random import choice

aluno_1 = str(input('\nInforme o nome dos quatro alunos participantes do sorteio.\n\nAluno 1: '))
aluno_2 = str(input('\nAluno 2: '))
aluno_3 = str(input('\nAluno 3: '))
aluno_4 = str(input('\nAluno 4: '))

sorteado = choice([aluno_1, aluno_2, aluno_3, aluno_4])

print('\n\nO aluno sorteado foi {}!'.format(sorteado))
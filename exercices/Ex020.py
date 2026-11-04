''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

from random import sample

aluno_1 = str(input('\nInforme o nome dos quatro alunos participantes do sorteio.\n\nAluno 1: '))
aluno_2 = str(input('\nAluno 2: '))
aluno_3 = str(input('\nAluno 3: '))
aluno_4 = str(input('\nAluno 4: '))

sorteio = sample([aluno_1, aluno_2, aluno_3, aluno_4], k=4)

print('\n\nEm ordem crescente, os sorteados foram {} !.'.format(sorteio))
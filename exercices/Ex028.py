'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randrange

num_sorteado = randrange(6) #Sorteia um número de 0 à 5, também é viável o uso do "radint(0,5)"
n = int(input('\nO programa irá sortear um número de "0 à 5". Caso seja coincidente ao seu, você ganhou!\n\nNúmero: '))
print('\nO número sorteado foi {}!'.format(num_sorteado))
if n == num_sorteado:
    print('\nVocê ganhou! Reinvidique seu prêmio.')
else:
    print('\nQue pena! Você não foi sorteado.')
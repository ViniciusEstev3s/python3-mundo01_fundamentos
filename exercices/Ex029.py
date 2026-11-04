'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite'''

velocidade = float(input('\nInforme a velocidade(Km\h) do veículo, o programa irá fiscalizar-la.\n\nVelocidade: '))
if velocidade > 80 :
    multa = (velocidade - 80) * 7
    print('\nO senhor(a) ultrapassou o limite de velocidade e foi multado!\n\nValor da multa: R${:.2f}.'.format(multa))
else:
    print('\n0 senhor(a) está dentro dos limites de velocidade, continue assim!')
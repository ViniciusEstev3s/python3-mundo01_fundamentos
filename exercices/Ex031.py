'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200km e R$0,45 para viagens mais longe.'''

distancia_km = float(input('\nInforme a distancia(km) de sua viagem, iremos calcular o custo total.\n\nDistância: '))
if distancia_km <= 200 :
    custo = distancia_km * 0.5
    print('\nO custo total de sua viagem de {:.1f}km, foi de R${:.2f}.'.format(distancia_km, custo), end='')
    print(' Sendo assim, R$0,50 por km.')
else:
    custo = distancia_km * 0.45
    print('\nO custo total de sua viagem de {:.1f}km, foi de R${:.2f}.'.format(distancia_km, custo), end='')
    print(' Sendo assim, R$0,45 por km.')
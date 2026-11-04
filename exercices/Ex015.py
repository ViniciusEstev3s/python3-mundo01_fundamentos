# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print('\nInforme a distância percorrida em Km e a quantidade de dias em que o carro foi alugado para que o gasto seja calculado.')
distancia_km = float(input('\nDistância percorrida em Km: '))
aluguel_dias = int(input('\nDias alugados: '))
print('\nApós percorrer {:.1f}km por {} dias, o gasto total com aluguel e consumo '.format(distancia_km, aluguel_dias), end='')
print('do carro foi de R${:.2f}.'.format((distancia_km*0.15)+(aluguel_dias*60)))

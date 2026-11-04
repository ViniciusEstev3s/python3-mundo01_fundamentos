# Escreva um programa que leia um valor em metros e o exiba convertdo em centímetros e milímetros.

print('\nInforme uma metragem, a própria será convertida em centímetros e milímetros.')
m = float(input('\nMetro(s): '))
print('\nVocê informou {:.2f} metro(s), que são {:.2f} centímetro(s) ou {:.2f} milímetro(s).'.format(m, m*100, m*1000))

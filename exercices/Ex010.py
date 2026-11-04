# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considera US$1.00 = R$3.27

capital = float(input('\nInforme seu capital para que o próprio seja convertido em dolar.\n\nCapital em Reais: R$'))
print('\nO capital de R${:.2f} equivale a ${:.2f}!.'.format(capital, capital/3.27))

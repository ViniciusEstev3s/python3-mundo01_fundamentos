# Faça um algoritmo ue leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('\nInforme o preço de um produto, será exibido um novo preço com 5% de desconto.\n\nPreço: R$'))
desconto5 = produto - (produto*0.05)
print('O produto informado, de valor R${:.2f}, passou por um desconto de 5%, valendo assim, R${:.2f}!.'.format(produto, desconto5))

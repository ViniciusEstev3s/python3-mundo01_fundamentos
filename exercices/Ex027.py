''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome
separadamente.

Ex: Ana Maria de Souza:
Primerio: Ana;
Ultimo: Souza. '''

nome = str(input('\nInforme o nome completo de uma pessoa, o programa exibirá o primeiro e último nome.\n\nNome: '))
print('\nPrimeiro nome: {}.'.format(nome.split()[0]))
print('\nÚltimo nome: {}.'.format(nome.split()[len(nome.split())-1]))
''' Na linha 10, dentro dos colchetes, determinei que seria fatiado o comprimento da variável nome, dividida em cadeia
de strings, subtraída por um. Esta ação faz com que seja contado o total de cadeias de caracteres da variável gerados 
pelo ".split()", e para adaptação de contagem de posição de strings utilizamos o "-1". '''
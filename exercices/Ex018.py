# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('\nInforme um ângulo em graus centígrados, exibiremos o seno, cosseno e tangente.\n\nÂngulo: '))
ang = radians(ang) #Transformando graus em radianos para que seja feito o calculo de sin, cos e tan.
print('\nSeno: {:.2f}°\nCosseno: {:.2f}°'.format(sin(ang), cos(ang)))
print('Tangente: {:.2f}°'.format(tan(ang)))

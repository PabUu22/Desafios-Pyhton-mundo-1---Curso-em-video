#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tg = tan(radians(angulo))
print('O valor do seno de {:.2f} é igual á {:.2f}'.format(angulo, seno))
print('O valor do cosseno de {:.2f} é igual á {:.2f}'.format(angulo, coss))
print('O valor da tangante de {:.2f} é igual á {:.2f}'.format(angulo, tg))
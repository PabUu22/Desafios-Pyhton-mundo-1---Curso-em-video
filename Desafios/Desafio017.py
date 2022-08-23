#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
Hi = ((math.pow(co,2)) + (math.pow(ca,2)))**(1/2) 
print('Valor da Hipotenusa é {:.2f}'.format(Hi))
# o modulo hypot poderia ser usado no lugar de toda expreção na linha 5, da seguinte formar: math.hypot(co, ca)

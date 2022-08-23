# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos não podem formar um triangulo')

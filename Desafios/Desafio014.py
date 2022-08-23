#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe uma temperatura em Celsius: '))
F = 9 * c / 5 + 32
print('A temperatura de {} °C, corresponde a {} °F'.format(c, F))
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Numero = int(input('Digite um número para saber se é impar ou par: '))

Resultado = Numero % 2 # se o resta da divisão de um numero inteiro for 1, logo ele é um número impar.

if Resultado == 1:
    print('O número {} é impar'.format(Numero))
else:
    print('O número {} é par'.format(Numero))

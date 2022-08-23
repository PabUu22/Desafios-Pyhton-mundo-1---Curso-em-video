#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n1 = float(input('Digite um valor: ' ))
r =  trunc(n1)
print('Valor digitado foi {}, seu valor inteiro é {}'.format(n1, r))
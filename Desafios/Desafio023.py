#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n1 = int(input('Digite um numero: '))
print('Esse numero tem {} unidades'.format (n1 // 1 % 10 ))
print('Esse numero tem {} Dezenas'.format (n1 // 10 % 10 ))
print('Essse número tem {} Centenas'.format (n1 // 100 % 10 ))
print('Esse número tem {} Milhar'.format(n1 // 1000 % 10))

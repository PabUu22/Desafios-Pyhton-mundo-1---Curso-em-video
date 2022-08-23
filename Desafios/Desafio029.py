# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual o valor atual da velocidade do carro? '))

if velocidade >= 80:
    print('Multado!!!, você ultrapassou 80km/h')
    print('E deverar pagara uma multa de R${:.2f}'.format((velocidade-80)*7))
    print('Por favor deminua a velocidade!')
else:
    print('Tudo tranquilo, diriga com segurança!')
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

Km = float(input('Digite a distancia em km da viagem: '))

if Km <= 200:
    print('Valor da viagem custarar R${:.2f}'.format(Km * 0.50))
else:
    print('Valor da viagem custarar R${:.2f}'.format(Km * 0.45))

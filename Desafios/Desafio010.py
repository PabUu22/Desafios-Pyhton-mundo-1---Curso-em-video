#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# valor do dolar 5,41

Real = float(input('Quanto você tem na carteira? R$ '))
print('Com o valor de {:.2f} R$, você poderar comprar {:.2f} US$'.format(Real, (Real / 5.41)))
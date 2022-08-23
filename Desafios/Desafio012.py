#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Prodt = float(input(' Digite o valor do produto: '))
des = (Prodt * 5 /100)
vf = (Prodt - des)
print('Seu produto custa {:.2f} R$, com desconto de 5% custarar {:.2f}'.format(Prodt, vf))
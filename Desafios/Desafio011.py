#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
área = (Largura * Altura)
print('Sua parede tem a dimensão de {:.2f} x {:.2f}, e sua área é de {}m²'.format(Largura, Altura, área))
print ('Para pintar essa parede você precisarar de {}L'.format(área / 2))
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

md = float(input('Digite o valor em Metros! '))
cm = md * 100
mm = md * 1000
print("O valor de {} metros em centimetros é {}, e em Milimetro {}".format(md, cm, mm))
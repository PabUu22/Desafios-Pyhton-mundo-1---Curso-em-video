#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep

salario = float(input('Digite o salario do funcionario: '))

print('Analisando...')
sleep(2)

if salario >= 1250:
    aumento = salario * 10 / 100
    print('com ajuste salarial de 10%, o funcionario(a) receberar R$:{:.2f}'.format(aumento + salario))
else:
    aumento = salario * 15 / 100
    print('Com um lasário inferior a R$:1250.00')
    print('O ajuste salarial é de 15%, o funcionario(a) receberar R$:{:.2f}'.format(aumento + salario))

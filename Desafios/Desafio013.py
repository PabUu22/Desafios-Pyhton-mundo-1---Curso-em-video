# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salario do funcionario:R$ '))
aumento = (salario * 15/100)
ajuste = (salario + aumento)
print ('O funcionario possui o salario de {} R$, com reajuste de 15% receberar {:.2f}'.format(salario, ajuste))
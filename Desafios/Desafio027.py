#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
print('Muito praser {}, estamos analisando seu nome...'.format(nome))
pn = nome.split()
print('Seu primeiro nome é {}'.format(pn[0]))
print('Seu ultimo nome é {}'.format(pn[len(pn)-1]))
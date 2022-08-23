#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('O nome digitado com todas as letras maiúculas fica: {}'.format(nome.upper()))
print('Já com letras minúsculas fica: {}'.format(nome.lower()))
print('A quantidade de letras total é {}'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))

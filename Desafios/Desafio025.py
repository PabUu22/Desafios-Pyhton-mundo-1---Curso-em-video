#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nom = str(input('Qual é seu nome? ')).strip()
print('No seu nome tem Silva? {}'.format('SILVA' in nom.upper()))
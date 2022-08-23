#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Onde vc nasceu? ')).strip()
Y=cidade.upper()
r ='SANTO' in Y [:5]
print(r)
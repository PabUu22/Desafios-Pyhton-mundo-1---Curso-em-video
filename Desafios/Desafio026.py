#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
fm = frase.upper()
print('A letra A aparece {} vezes na frase'.format(fm.count('A')))
print('A primeira letra A está na posição {}'.format(fm.find('A')+1))
print('A ultima letra A está na posição {}'.format(fm.rfind('A')+1))
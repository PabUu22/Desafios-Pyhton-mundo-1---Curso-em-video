#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

N1 = float(input('Primeira nota do aluno:'))
N2 = float(input('Segunda nota do aluno:'))
M = ((N1 + N2) /2)
print('A media entre {:.1f} e {:.1f} é igual {:.1f}'.format(N1, N2, M))
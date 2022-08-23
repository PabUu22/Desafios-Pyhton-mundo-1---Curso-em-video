#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep # Biblioteca de "time"

print('Vamos jogar um jogo?')
print('Estou pensando em um numero entre 0 e 5, consegue advinhar? ')
NUM = int(input('Digite o numero que estou pensando: ')) # Numero sujerido pelo jogador
Computador = randint(0,5) #Faz um sorteio entre 0 e 5
print('Processando...')

sleep(3)   #Time de uma linha para outra

if NUM == Computador:
    print('Parabens Você acertou!!!')
else:
    print('Voce não conseguiu!!!')
'''
Ecreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuario tentar
descobrir o número ecolhido pelo computador.

O programa deverá escrever na tela
se o usuario venceu ou perdeu?
'''
'''
import random
print('Vou pensar em um número inteiro de 0 a 5. tente adevinhar...')
print('Em que número eu pensei?')
number = random.randint(1,5)
num = int(input('Digita um número inteiro de 0 a 5: '))

if number == num:
    print('PARABÉNS VOCÊ VENCEU')
else:
    print('GAME OVER, TENTE NOVAMENTE')
print(f'O número inteiro é: {number}')'''

from random import randint
from time import sleep
computador = randint(1, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} não no número {jogador}') 

'''
Cria um programa que faça o computador jogar Jokempô com você.
'''
import random
from time import sleep
print(f'{' JOKENPÔ ':=^40}')
print('''OPCOES:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')

computador = random.randint(0,2)
jogador = int(input('Faça sua jogada: '))
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!!!')

if computador == jogador:
    print(f'EMPATE! Ambos escolheram {computador}')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('PARABÊNS! Você venceu')
    print(f'Eu joguei {computador} e você jogou {jogador}')
else:
    print('GANHEI! TENTE NOVAMENTE!')
    print(f'Eu joguei {computador} e você jogou {jogador}')
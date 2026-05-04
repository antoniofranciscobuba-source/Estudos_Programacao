import random
from time import sleep
print(f'{' JOKENPÔ ':=^40}')

print('''OPÇÕES:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
jogador = int(input('Faça sua jogada: '))

print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!!!')

if 0 <= jogador <= 2:
    if computador == jogador:
        print(f'EMPATE! Ambos jogaram {itens[computador]}')
    elif (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
        print('PARABÊNS! Você venceu!')
        print(f'Eu joguei {itens[computador]} e você jogou {itens[jogador]}')
    else:
        print('GANHEI! TENTE NOVAMENT!')
        print(f'Eu joguei {itens[computador]} e você jogou {itens[jogador]}')
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE!')
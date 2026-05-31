'''
Faça um programa que joga par ou impar com o computador. O jogo só será interrompido 
quando o jogador PERDER, mostrando o tatal de victorias consecutivas que ele conqueistou
no final do jogo.
'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computer = randint(0, 5)
    total = jogador + computer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e eu joguei {computer}. Total {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU✅')
            v += 1
        else:
            print('VOCÊ PERDEU❌')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU✅')
            v += 1
        else:
            print('VOCÊ PERDEU❌')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {v} vezes')
'''
Melhora o jogo do desafio 028 onde o computador vai 'pensar'
em um número entre 0 e 10. Só que agora o jogador vai tentar 
advinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.
'''
from random import randint
from time import sleep 
count = 0
computer = randint(0, 10)
jogador = 11
print('\033[33m=-\033[m' * 20)
print('🤖 \033[32mPensei em um número entre 0 a 10...\033[m')
print('\033[33m=-\033[34m' * 20)
print('\033[32mTENTE ADIVINHAR...😉\033[m')

while jogador != computer:
    jogador = int(input('Faça a sua jogada: '))
    print('\033[36mANALISANDO...\033[m')
    sleep(0.5)
    count += 1
    if jogador != computer:
        print('❌\033[31mERROU! Tente novamente!\033[m')
        sleep(0.5)
    if jogador < computer:
        print('Mais...')
    elif jogador > computer:
        print('Menos...')
        

print(f'✅ \033[32mACERTOU!\033[m Eu joguei {computer} e voçê jogou {jogador}.')
print(f'Você tentou {count} vezes até conseguir!')

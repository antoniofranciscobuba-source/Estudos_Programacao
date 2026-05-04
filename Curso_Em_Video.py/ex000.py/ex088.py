'''
Faça um programa que ajuda o jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre um e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{' JOGUE NA MEGA SENA' :^30}')  
print(f'-' * 30)
quant = int(input('Quantos números você quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'{f'-=-=-= Sorteando {quant} números =-=-=- ':^30}')

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
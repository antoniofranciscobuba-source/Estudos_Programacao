'''
Faça um programa que leia um número inteiro e diga 
se ele é ou não um número primo.
'''
n = int(input('Digite um valor: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {n} foi dividido {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
      
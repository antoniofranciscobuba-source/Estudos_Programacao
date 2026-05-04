'''
Crie um programa que vai gerar 5 números aleátorios e vai colocalas em uma tupla.
Depois disso mostre a listagem de números, e também indique o maior e o menor que estão na Tupla.
'''
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print(f'Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

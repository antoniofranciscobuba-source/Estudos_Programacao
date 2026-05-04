"""
Cria um programa que leia um número Real qualquer pelo teclado 
e mostre na tela a sua porção inteira exemplo: 7.234 >>> 7
"""

num = float(input('Digite um número: '))
print(f'O número real {num} passa para inteiro {int(num)}')

import math
num = float(input('Digite um valor: '))
print(f'O número Real {num} passa para o número inteiro {math.trunc(num)}')

from math import trunc
number = float(input('Digite um valor: '))
print(f'O valor digitado é {number} e a sua porção inteira é {trunc(number)}')

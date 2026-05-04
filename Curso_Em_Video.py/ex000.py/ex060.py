'''
Faça um programa que leia um número qualquer e mostre o seu factorial:
EX: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
import math
n = int(input("Digite um valor: "))
print(math.factorial(n))

n = int(input('Digite um vlaor: '))
resultado = 1
contador = n
while contador > 0:
    resultado *= contador
    contador -= 1
print(f'O factorial de {n} é {resultado}')
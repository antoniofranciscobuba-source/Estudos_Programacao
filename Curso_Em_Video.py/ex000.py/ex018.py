'''
Faça um programa que leia um Ángulo qualquer e mostre
e mostre na tela o valor do seno cosseno e tangente
deste Ángulo.
'''
import math
ang = float(input('Digite o Ângulo em graus: '))
rad = math.radians(ang)
print(f'valor seno {math.sin(rad):.2f}')
print(f'valor cosseno {math.cos(rad):.2f}')
print(f'valor tangente {math.tan(rad):.2f}')

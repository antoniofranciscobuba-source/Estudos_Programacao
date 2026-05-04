"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo rectangulo,
calcule e mostre o comprimento da Hipotenusa
"""

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'O comprimento do cateto oposto {cateto_oposto} e o cateto adjacente {cateto_adjacente} é igual a {hipotenusa:.2f}')

# A forma de calcular com o modulo math

from math import hypot
co = float(input('Digite o CO: '))
ca = float(input('Digite o CA: '))
print(f'A Hipotenusa é igual a: {hypot(co, ca):.2f}')
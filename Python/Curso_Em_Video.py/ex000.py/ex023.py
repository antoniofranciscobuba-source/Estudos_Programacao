'''
Faça um programa que leia de 0 a 9999 e mostre a tela
cada um dos digitos separados.
Ex: 
digite um número: 1834
unidade: 1
dezena: 8
centena: 3
milhar: 4
'''
n = int(input('Digite um número de quatro digitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''
Desenvolva um programa que leia três números inteiros 
e mostre a soma apenas daqueles que forem pares, se o valor digitado
for impar, desconsidere-o.
'''
'''
soma = 0
n1 = int(input('Primeiro valor: '))
if n1 % 2 == 0:
    soma += n1
n2 = int(input('Segundo valor: '))
if n2 % 2 == 0:
    soma += n2
n3 = int(input('Terceiro valor: '))
if n3 % 2 == 0: 
    soma += n3
print(f'A soma dos valores pares digitado é {soma}')'''


soma = 0 
count = 0
for i in range(0, 3):
    n = int(input('Digite o valor: '))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'Você informou {count} números pares e a soma foi {soma}')



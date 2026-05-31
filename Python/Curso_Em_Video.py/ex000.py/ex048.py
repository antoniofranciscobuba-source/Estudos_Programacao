'''
Faça um programa que calcule a soma de todos os números impares
que são multiplos de três e que se encontram no intervalo de 1 até 500.
'''
'''
print('Soma de números pares: ')
for i in range(1,500):
    if i % 2 == 0:
        print(i + i)'''

soma = 0
count = 0
for i in range(1,  500):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        count += 1
print(f'A soma de todos os {count} valores solicitados é {soma}')
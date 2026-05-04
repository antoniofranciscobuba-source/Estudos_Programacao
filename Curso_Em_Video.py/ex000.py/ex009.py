#Faça um programa que mostre um número inteiro 'Qualquer' e mostre na tela a sua tabuada
'''
n = int(input('Digite um número: '))
s1 = n * 1
s2 = n * 2
s3 = n * 3
s4 = n * 4
s5 = n * 5
s6 = n * 6
s7 = n * 7
s8 = n * 8
s9 = n * 9
s10 = n * 10
s11 = n * 11
s12 = n * 12
print(f'A tabuada de {n} é:\n {s1} \n {s2} \n {s3} \n {s4} \n {s5} \n {s6} \n {s7} \n {s8} \n {s9} \n {s10} \n {s11} \n {s12}')

#Segunda forma
n = int(input('Digite um número: '))
s1 = n * 1
s2 = n * 2
s3 = n * 3
s4 = n * 4
s5 = n * 5
s6 = n * 6
s7 = n * 7
s8 = n * 8
s9 = n * 9
s10 = n * 10
s11 = n * 11
s12 = n * 12
print('-' * 12)
print(n, 'X 1 =', s1 )
print(n, 'X 2 =', s2 )
print(n, 'X 3 =', s3 )
print(n, 'X 4 =', s4 )
print(n, 'X 5 =', s5 )
print(n, 'X 6 =', s6 )
print(n, 'X 7 =', s7 )
print(n, 'X 8 =', s8 )
print(n, 'X 9 =', s9 )
print(n, 'X 10 =', s10 )
print(n, 'X 11 =', s11 )
print(n, 'X 12 =', s12 )
print('-' * 12)
'''
# Mas uma outra forma
number = int(input('Digite um numero para a Tabuada: '))
print('*' * 12)
print(f'{number} X {1:2} = {number * 1}')
print(f'{number} X {2:2} = {number * 2}')
print(f'{number} X {3:2} = {number * 3}')
print(f'{number} X {4:2} = {number * 4}')
print(f'{number} X {5:2} = {number * 5}')
print(f'{number} X {6:2} = {number * 6}')
print(f'{number} X {7:2} = {number * 7}')
print(f'{number} X {8:2} = {number * 8}')
print(f'{number} X {9:2} = {number * 9}')
print(f'{number} X {10:2} = {number * 10}')
print(f'{number} X {11:2} = {number * 11}')
print(f'{number} X {12:2} = {number * 12}')
print('*' * 12)
'''
Faça um programa que leia 3 números e mostre qual é o maior 
e qual é o menor.
'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Treiceiro número: '))
print('Processando...')
sleep(1.5)
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#ao contrario
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')

    





'''
if (n1 < n2 and n1 < n3) or (n2 < n1 and n2 < n3) or (n3 < n1 and n3 < n2):
    print('O número é o menor')
else:
    print('O número é maior')'''

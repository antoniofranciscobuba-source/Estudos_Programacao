'''
Faça um programa que leia uma frase pelo teclado 
e mostre:

*Quantas vezes aparece a letra 'A'

*Em que posição ela aparece pela primeira vez

*Em que posição ela aparece pela ultima vez

'''
fra = str(input('Escreva uma frase: ')).strip()
frase = fra.upper()
print(f'Na frase aparece {frase.count('A')} vezes a letra "A"')
print(f'A letra "A" aparece primeiro na posição {frase.find('A') + 1}')
print(f'A letra "A" aparece pela ultima vez na posição {frase.rfind('A') + 1}')
'''
Dezenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla, no final mostre:
A) Quantas vezes apareceu o valor 9.
B) E que posção foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultimo: ')))
print(f'Os valores armazenados são: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 foi digitada na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitada em nenhuma posção.')
print('Os valores pares digitados são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
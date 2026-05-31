'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista,
no final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma lista com as pessoas mais pesadas.
C) Uma listangem com as pessoas mais leves.
'''
dado = []
pessoa = []
mai = men = cont = maisp =0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: kg '))
    dado = [nome, peso]
    pessoa.append(dado[:])
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for p in pessoa:
    cont += 1
print('-=' * 25)
print(f'Os dados foram: {pessoa}')
print(f'Foram cadrastadas {cont} pessoas.')
for p in pessoa:
    if p == pessoa[0]:
        mai = men = p[1]
    else:
        if p[1] > mai:
            mai = p[1]
        if p[1] < men:
            men = p[1]
print(f'O maior peso foi de {mai}kg. Peso de: ', end='')
for p in pessoa:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi {men}kg. Peso de: ', end='')

for p in pessoa:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print('\n' + '=' * 30)
'''
Crie um programa onde o usuário possa digitar 7 valores númericos, e cadatre-as em uma
lista única que mantenha separados os valores pares e Ímpares, no final mostre os valores
pares e ímpares na ordem crescente.
'''
num = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-=' * 25)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

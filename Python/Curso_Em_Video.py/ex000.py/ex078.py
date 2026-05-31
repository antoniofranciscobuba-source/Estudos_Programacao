'''
Faça um porgrama que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o menor e o maior valor digitados e as suas 
respectivas posições na lista.
'''
valores = []

for _ in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores: {valores}')    
print(f'O maior valor da lista foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'E o menor valore da lista foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()

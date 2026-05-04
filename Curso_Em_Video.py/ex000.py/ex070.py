'''
Crie um programa que leia o nome e o preço de vários produtos, o programa deverá 
perguntar se o usuário vai continuar. no final, mostre:
A)Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000 na compra.
C)Qual é o nome do produto mais barato.
'''
efe = '-' * 30
print(efe)
print(f'{'>' * 5} LOJA DA GRACE {'<' * 5}')
print(efe)

produto = ' '
preço = total = tot_produto = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: €'))
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        tot_produto += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if resp == 'N':
        break

print(f'{' FIM DO PROGRAMA ':=^40}')
print(f'O total da compra foi €{total:.2f}')
print(f'Temos {tot_produto} produtos custando mais de €1000.00')
print(f'O produto mais barato foi {barato} e custa €{menor} ')
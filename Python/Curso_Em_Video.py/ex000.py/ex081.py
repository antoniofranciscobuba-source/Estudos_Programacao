'''
Cria um porgrama que vai ler vários números e vai colocar em uma lista.
Depois disso mostra:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break   
print('-=' * 20)
valores.sort(reverse= True)
print(f'você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
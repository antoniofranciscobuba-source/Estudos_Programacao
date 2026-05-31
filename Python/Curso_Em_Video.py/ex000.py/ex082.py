'''
Crie um programa que leia vários números e colocar em uma lista. 
depois disso crie duas listas extras, que vão conter apenas os valores pares 
e os valores impares digitados, respectivamente.
Ao final, mostre os conteúdos das três listas geradas.
'''
valores = []
lista1 = []
lista2 = []
pares = inpar = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = ' '
    if num % 2 == 0:
        lista1.append(num)
    else:
        
        lista2.append(num)
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 25)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {lista1}')
print(f'A lista de ímpares é {lista2}')

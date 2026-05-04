'''
Cria um programa que leia vários números inteiro pelo teclado.
No final da execução mostre a média entre todos os valores 
e qual foi o maior e o menor valores lidos. O programa deve perguntar
para o usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'Ss'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um múmero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior =num
        if num < maior:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
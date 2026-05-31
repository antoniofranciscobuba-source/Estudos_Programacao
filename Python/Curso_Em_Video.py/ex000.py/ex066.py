'''
Crie um programa que leia varios números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).
'''
count = soma = num = 0 
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'A soma dos {count} valores foi {soma}!')
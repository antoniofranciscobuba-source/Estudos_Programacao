'''
Crie um programa que mostre a tabuada de vários números, um de cada vez
para cada valor digitado pelo usuário. O programa será interrompido 
quando o número solicitado for negativo.
'''
from time import sleep
num = 0
while True:
    print(f'-'* 35)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'* 35)
    if num < 0:
        break
    for count in range(1, 13):
        print(f'{num} X {count:2} = {num * count}')
print('PROGRAMA TABUADA ENCERRANDO...')
sleep(1.5)
print('Volte sempre!')
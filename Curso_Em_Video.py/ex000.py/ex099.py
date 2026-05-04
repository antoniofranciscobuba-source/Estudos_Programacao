'''
Faça um programa que tenha uma função chamada maior, que recebe vários parâmetros
com valores inteiros.
Seu programatem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O valore maior informado foi {maior}.')
#Programa principal
maior(1, 5, 6, 2, 6, 8, 3, 4)
maior(4, 6, 2, 6, 8)
maior(5, 6, 8, 2, 9, 2)
maior(1, 6, 3, 6)
maior(4, 7, 5)
maior(7, 2)
maior()
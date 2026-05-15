'''
Faça um programa que tenha uma função chamada contador(), que receba
3 parâmentros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens atravez a função criada:

A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma gontagem Personalizada.
'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)    
    print(f'contagem de {i} até {f} de {p} em {p}:')
    sleep(0.2)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini= int(input('Inicio: '))
fi= int(input('Fim: '))
pas= int(input('Passo: '))
contador(ini, fi, pas)
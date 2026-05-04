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
    print('-=' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, f+1, p):
        print(f'{c} ', end='')
        sleep(0.5)
    print('FIM')


contador(i=int(input('Inicio: ')), f=int(input('Fim: ')),  p=int(input('Passo: ')))










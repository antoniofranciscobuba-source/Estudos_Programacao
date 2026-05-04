'''
Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.
'''
from time import sleep
from datetime import date
print('-=-' * 25)
print('Olá! Se quiseres analizar se o ano é BISSEXTO ou NÃO eu posso te ajudar!')
print('-=-' * 25)

ano = int(input('Que ano você quer analizar? '))
if ano == 0:
    ano = date.today().year
    
print(f'ANALISANDO O ANO {ano}...')
sleep(1.5)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')

'''
if ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
elif ano % 100 == 0:
    print(f'O ano {ano} não é BISSEXTO')   
elif ano % 4 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')
    '''

    
'''
ano = int(input('Digite qualquer ano: '))

# Aqui está a mágica em uma linha:
resultado = "BISSEXTO" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else "NÃO BISSEXTO"

print(f'O ano {ano} é {resultado}')
'''
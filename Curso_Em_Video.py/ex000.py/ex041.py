'''
A confederação nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre, a sua categoria de acordo com a idade:

- Até 9 anos: MERIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date
from time import sleep
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
print('ANALISANDO SUA CATEGORIA...')
sleep(1.0)
if idade <= 9:
    print('Classificação: MERLIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

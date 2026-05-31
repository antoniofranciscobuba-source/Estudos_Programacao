'''
Faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
-Se ja passou a hora de alistamento
-Se ja passou o tempo de alistamento

Seu programa também deve mostrar o tempo que faltou
ou o tempo que passou do prazo.
'''
from datetime import date
atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nasc
print('''Genero: 
      [M] Masculino
      [F] Femenino''')
gen = (input('Qual é o seu genero? ')).upper().strip()

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if 'M' == gen:
    print('VERIFICANDO ALISTAMENTO MILITAR...')
    if idade == 18:
        print('Voçê tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} para o alistamento.')
        ano = atual + saldo
        print(f'Você deve se alistar em {ano}.')    
    else:
        saldo = idade - 18
        print(f'Voçê já deveria se alistar a {saldo} anos.')
        ano = atual - saldo
        print(f'O ano de alistamento foi em {ano}.')
elif 'F' == gen:
    print('O alistamento militar não é obrigatório para mulheres.')        
else:
    print('OPÇÃO INVÁLIDA! Por favor digite apenas [M] ou [F].')


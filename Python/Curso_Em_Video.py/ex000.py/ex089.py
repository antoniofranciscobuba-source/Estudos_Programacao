'''
Crie um programa que leia nome e duas notas de vários alunos, e guarde tudo em uma lista
composta, no final mostre um boletim conténdo a média de cada um e permita que o usuário 
possa mostrar a nota de cada aluno individualmente 
'''
from time import sleep
ficha = []
cont = 0
while True:
    name = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([name, [n1, n2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 25)
print(f'{'No.':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-' * 30)
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if aluno == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if aluno <= len(ficha) -1:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
    else:
        print(f'O aluno {aluno} não faz parte da lista. Tente novamente!')
print('<<<< VOLTE SEMPRE! >>>>')
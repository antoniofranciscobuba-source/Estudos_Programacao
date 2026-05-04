'''
O mesmo professor  do desafio anterior, quer sortear a ordem
de apresentação de trabalhos dos alunos. Faça um programa
que leia os nomes dos quatros alunos e mostra a ordem sorteda.
'''

import random

alunos = []
for i in range(1, 5):
    name = input(f'{i} aluno: ')
    alunos.append(name)
escolhido = random.choices(alunos)
print(f'O aluno ecolhido é {escolhido}')


import random

alunos = []
for i in range(1,5):
    name = input(f'{i} aluno: ')
    alunos.append(name)
ordem = random.sample(alunos, k=4)

print(f'Ordem de apresentação: {ordem}')

# A forma junior 

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Treiceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

print('Ordem dos alunos: ')
print(random.sample(lista, k=4))

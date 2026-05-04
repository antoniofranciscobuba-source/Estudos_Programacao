'''
Faça um programa que leia o nome e a média de um aluno, guardando também a situação
em um dicionário, no final mostra o conteúdo da estrutura na tela.
'''
dado = []
for c in range(0, 1):
    aluno = {}
    aluno['Nome'] = str(input('Nome: '))
    aluno['Média'] = float(input(f'Média de aluno {aluno['Nome']}: '))
    if aluno['Média'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif 5 <= aluno['Média'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Reprovado'
    dado.append(aluno.copy())
print('-=' * 15)
for a in dado:
    for k, v in a.items():
        print(f'- {k} é igual a {v}')
    print('-' * 20)
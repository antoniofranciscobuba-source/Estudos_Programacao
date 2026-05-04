'''
Cria um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final
de acordo com a media atingida:

- Média abaixo de 5.0 REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior APROVADO
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'\n Primeira Nota: {n1} \n Segunda Nota: {n2} \n Média: {media:.2f} \n')
cores = {'limpa': '\033[m',
         'azul': '\033[4;36;40m',
         'vermelho': '\033[4;31m',
         'verde': '\033[4;32m'}
if media < 5.0:
    print(f'{cores["vermelho"]}REPROVADO{cores["limpa"]}')
elif 5.0 <= media <= 6.9:
    print(f'{cores["azul"]}RECUPERAÇÃO{cores["limpa"]}')
else:
    print(f'{cores["verde"]}APROVADO{cores["limpa"]}')
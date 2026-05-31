'''
Cria um programa que aprova o imprestimo bancario
para a compra de uma casa. O programa vai perguntar 
o valor da casa, o salario do comprador e quantos anos 
eles vão pagar.

Calcule o valor da prestação mensal, sabendo que ele
não pode exceder 30% do salário ou então o emprestimo
será negado.
'''
from datetime import date
v_casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
ano = int(input('Quantos anos quer pagar a casa? '))

cores = {'limpa': '\033[m',
         'azul': '\033[4;36;40m',
         'vermelho': '\033[4;31m',
         'verde': '\033[32m'}

meses = ano * 12
prestacao = v_casa / meses
limite = salario * 30 / 100
print(f'Para pagar uma casa de R${v_casa:.2f} em {ano} anos...')
print(f'A pretação será de R${prestacao:.2f}')

if prestacao <= limite:
    print(f'{cores["azul"]}EMPRÉSTIMO PODE SER CONCEDIDO{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}EMPRÉSTIMO NEGADO!{cores["limpa"]} A prestação excede 30% do salário.')

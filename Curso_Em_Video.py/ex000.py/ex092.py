'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadraste-os (com idade)
Em um dicionario se por acaso o CTPS for diferente de ZERO, o dicionario recebera também o ano de
contratação e salário, calcule e acrescente, elem da idade, com quantos anos a pessoa vai se aposentar?
'''
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nsc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nsc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    print('-=' * 30) 
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
'''
pessoa = {'Nome': 'Jilson', 'Sexo': 'M', 'Idade': 33}
pessoa['peso'] = 60.99
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
for k, v in pessoa.items():
    print(f'{k} = {v}')

locadora = [{'Titulo': 'Matrix', 'Ano': 1999}, {'Titulo': 'Vaiana', 'Ano': 2020}, {'Titulo': 'Beekepeer', 'Ano': 2024}]
print(locadora[2]['Titulo'])'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for c in brasil:
    for e in c.values():
        print(f'{e}', end=' ')
    print()
'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campionato Brasileiro de Futebol,
na ordem de colocação, depois mostre:
A) Apenas os cincos primeiros colocados
B) Os ultimos quatros colocados na tabela 
C) Uma lista com os times em ordem alfabética 
D) Em que posição na tabela está o time chapecoense
'''
colocados = ('Palmeiras', 'Grêmios', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantio',
         'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('--- Lista de times Brasileirão ---')
print('=' * 15)
for t in colocados:
    print(t)
print('=' * 15)
print(f'Os cincos primeiro colocados são: {colocados[0:5]}')
print('-=' * 30)
print(f'Os ultimos quatros colocados são: {colocados[-4:]}')
print('-=' * 30)
print(f'====== A lista na ordem alfabética ====== \n{sorted(colocados)}')
print(f'O time CRUZEIRO está na posição {colocados.index('Cruzeiro') + 1}')
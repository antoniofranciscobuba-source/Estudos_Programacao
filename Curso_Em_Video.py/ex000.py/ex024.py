'''
Cria um programa que leia o nome da cidade
e diga se ela começa ou não com a palavra "SANTO"
'''
'''
cidade = input('Digita o nome da sua cidade: ')
print(f'Nome da cidade: {cidade}')
#print(f'O nome da sua cidade não começa com SANTO, {cidade.find('SANTO')}')

if cidade == 'SANTO':
    print(f'O nome da sua cidade começa com a palavra "SANTO" isso quer dizer: {cidade.find('SANTO')}')
else:
    print(f'O nome da sua cidade não começa com a palavra "SANTO" isso quer dizer: {cidade.find('SANTO')}')
'''

cidade = input('Digita o nome da sua cidade: ').strip()
cidade_m = cidade.upper()
if cidade_m[:5] == 'SANTO':
    print(f'A cidade {cidade} começa com SANTO!')
else:
    print(f'A cidade {cidade} não começa com SANTO')

# A forma que achei a mais facil de todas

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

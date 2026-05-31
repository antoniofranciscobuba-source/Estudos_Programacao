'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidades de gols feitos em cada partida. No final tudo isso 
ficará guardado em um dicionário, incluindo o total de gols feito durante 
o campeonato.
'''
dados = {}
gols = []
soma = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(0, partidas):
    gol = int(input(f'    Quantos gols na partida {c}? '))
    gols.append(gol)
    dados['gols'] = gols
    soma += gol
    dados['total'] = soma
print('-=' * 30)    
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados['nome']} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados['total']} gols.')
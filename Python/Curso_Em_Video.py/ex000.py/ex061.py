'''
Refaça o exercicio 051, lendo o primeiro termo e a razão de um PA
Mostrando os 10 primeiros termos da progressão usando a estrutura While.
'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro 
count = 1
while count <= 10:
    print(f'{termo} ➡  ', end='')
    termo += razão 
    count += 1
print('FIM')
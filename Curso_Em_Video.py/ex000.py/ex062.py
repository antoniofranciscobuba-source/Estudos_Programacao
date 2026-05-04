'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra que ele disser que quer mostrar
o 0 termo.
'''
print('Gerador de PA')
print('=-=' * 6)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print(f'{termo} 💨  ', end='')
        termo += razão
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quere mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

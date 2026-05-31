'''
Crie um programa que tenha uma tupla totalmente preenchida, com uma contagem com extensão de zoro até vinte.
Seu programa deverá ler um número pelo seu teclado entre 0 e 20, e mostrá-los por extensão
'''

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')   
    print(f'Você digitou o número {cont[n]}')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Programa finalizado. Volte sempre!')

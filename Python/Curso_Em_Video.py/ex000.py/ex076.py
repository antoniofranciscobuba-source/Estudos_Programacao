'''
Cria um programa que tenha uma tupla única com nomes de produtos e respectivos preços, na sequência.
No final, mostre uma listagem de preços organizado os dados em forma tabular.
'''
produto = ('Arroz', 43.55, 'Massa', 18.99, 'Laranja', 50.39, 'Laptop', 235.99, 'Tshert', 77.42,
           'Teclado', 86.88, 'Carregador', 45.93, 'Vela', 5.99, 'Mala', 66.37, 'Mouse', 39.80, 
           'Secador', 99.55, 'Lanterna', 20.69, 'Cabana', 530.99, 'Lenha', 9, 'Calça', 67.77)
print('-' * 40)
print(f'{' LISTA DE PRODUTOS ':^40}')
print('-' * 40)
for pos in range(0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<30}', end='')
    else:
        print(f'€{produto[pos]:>7.2f}')
print('-' * 40)
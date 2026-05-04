'''
Faça um programa que leia o peso de 5 pessas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
pes_maior = 0
pes_menor = 0
for pessoas in range(1, 6):
    peso = float(input(f'Peso da {pessoas} pessoa (Kg): '))
    if pessoas == 1:
        pes_maior = peso
        pes_menor = peso
    else:

        if peso > pes_maior:
            pes_maior = peso

        if peso < pes_menor:
            pes_menor = peso

print(f'O maior peso lido foi de {pes_maior}Kg')
print(f'O menor peso lido foi de {pes_menor}Kg')   
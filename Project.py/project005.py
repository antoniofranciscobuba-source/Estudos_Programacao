'''
Aprimore o exercicio anterior mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mai = par = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição: [{l}, {c}] '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    mai = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    mai = matriz[1][1]
elif matriz[1][2] > matriz[1][0] and matriz[1][2] > matriz[1][1]:
    mai = matriz[1][2]
else:
    print('⚠ Os valores são iguais por isso: ', end='')
print(f'O maior valor da segunda linha é: {mai}.')

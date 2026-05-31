'''
Refaça o Desafio 9 mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for.
'''
n = int(input('Digite um número: '))
if n > 0:
    for i in range(1, 13):
        print(f'{n} X {i:2} = {n * i}')
else:
    print('POR FAVOR, digite um número positivo!')   
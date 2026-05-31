'''
Cria um programa que mostre na tela todos os números 
pares que estão no intervalo entre 1 e 50.
'''
'''
print('Os números pares encontrados são: ')
for i in range(1,51):
    if i % 2 == 0:
        print(f'{i} é um número par')
'''       
print('Os números  (modo turbo): ')
for i in range(2,51, 2):
    print(f'{i} é um par')

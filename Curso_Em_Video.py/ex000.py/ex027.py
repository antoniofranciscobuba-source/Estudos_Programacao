'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
ex:Jilson Lin Buba
primeiro: Jilson
Ultimo: Buba
'''
'''
name = str(input('Digite o seu nome completo: ')).strip()
print(f'Nome completo: {name}')
print(f'Primeiro nome: {name.split()[0]} ')
print(f'Ultimo: {name.split()[-1]}')
'''

name = str(input('Digite o seu nome completo: ')).strip()
name_sep = name.split()
print(f'Nome completo: {name}')
print(f'Primeiro: {name_sep[0]}')
print(f'Ultimo: {name_sep[-1]}')
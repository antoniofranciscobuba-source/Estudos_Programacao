'''
Cria um programa que leia o nome completo da pessoa
e mostre na tela:

*O nome com todas letras Maiusculas
*O nome com todas menusculas
*Quantas letras ao todo sem considerar os espaços
*Quantas letras tem o primeiro nome
'''
name = str(input('Digite o nome completo: ')).strip()
print('Processando o nome...')
print(f'Seu nome completo é: {name}')
print(f'Seu nome em maiúscula é: {name.upper()}')
print(f'Seu nome em minúscula é: {name.lower()}')
print(f'O nome em todo tem {len(name)-name.count(' ')} letras')
#print(f'Seu primeiro nome tem {name.find(' ')} letras')
separa = name.split()
print(f'O seu Primeiro nome é {separa[0]} e ele tem {name.find(' ')} letras')


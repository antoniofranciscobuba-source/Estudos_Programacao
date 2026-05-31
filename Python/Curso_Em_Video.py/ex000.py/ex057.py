'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite 
os valores 'M' e 'F'. Casoe steja errado peça a digitação novamente
até ter um valor correto.
'''
'''
s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if s != 'M' and s != 'F':

        print(f'Dados invalídos. Por favor')
print(f'O sexo é {s}, Pode prosseguir a operação!' )
'''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

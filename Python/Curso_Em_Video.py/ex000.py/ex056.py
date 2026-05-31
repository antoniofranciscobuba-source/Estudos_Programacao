'''
Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa, mostre:

- A média da idade do grupo.
- Qual é o nome do homem mais velho.
-Quantas mulheres têm menos de 21 anos.
'''
soma_idade = 0
homem_m = 0
nome_velho = ''
mulh_m = 0
for pessoa in range(1, 5):
    print(f'-----{pessoa}ª-----')
    name = str(input('Nome: ')).strip()
    idade = int(input(f'Idade: '))
    soma_idade += idade
    print('''GENERO:
          [M] MASCULINO
          [F] FEMENINO''')
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()

    if sexo == 'M' and pessoa == 1:
        homem_m = idade
        nome_velho = name
    elif sexo == 'M' and idade > homem_m:
        homem_m = idade
        nome_velho = name
    if sexo == 'F' and idade < 20:
        mulh_m += 1
media = soma_idade / 4

print(f'A média da idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {homem_m} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulh_m} mulheres com menos de 20 anos.')
   
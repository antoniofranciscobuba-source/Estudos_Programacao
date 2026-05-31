'''
 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
 o programa deverá perguntar se o usuário quer ou não continuar, no final mostre:
 A) Quantas pessoas  tem mais de 18 anos. 
 B) Quantos homens foram cadastrados. 
 C)Quantas mulheres têm menos de 20 anos.
 '''
idade = tot_maior = tot_mulher = tot_homens = 0
print(f'{'-' * 22}\n CADASTRE UMA PESSOA \n{'-' * 22}')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if idade >= 18:
        tot_maior += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F':
        if idade < 20:
            tot_mulher += 1
    if resp == 'N':
        break
print(f'{'='* 10} FIM DO PROGRAMA {'=' * 10}')
print(f'Total de pessoas com mais de 18 anos: {tot_maior}')
print(f'Ao todo temos {tot_homens} homens cadastrados')
print(f'E temos {tot_mulher} mulheres com menos de 20 anos.')
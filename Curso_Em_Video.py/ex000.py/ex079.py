'''
Crie um programa onde o usuário pode digitar vários valores númericos e 
cadastra-os em uma lista. Caso o número já exista lá dentro ele não será 
adicionado. No final serão exibidos todos os valores únicos digitados, 
na ordem crescente.
'''
valores = []
while True:
    n =  int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...!✅')
    else:
        print('Valor duplicado. Não será adicionado!🚫')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()    
print(valores)

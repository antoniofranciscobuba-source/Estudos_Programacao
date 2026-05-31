'''
Cria um programa que leia um número inteiro qualquer e peça
para o usuário escolher, qual será a base da conversão:

1 - Para Binário
2 - Para Octal
3 - Para Exadecimal
'''
num = int(input('Digite um valor: '))
print('\nBases da converção:\n [1] Binário\n [2] octal \n [3] Hexadecimal')

opcao = input('Qual será a base da conversão? ')

match opcao:
    case '1':
        print(f'Binário {bin(num)[2:]}')
    case '2':
        print(f'Octal {oct(num)[2:]}')
    case '3':
        print(f'Hexadecimal {hex(num)[2:]}')
    case _: 
        print('OPÇÃO INVALIDA!')

'''
if opcao == '1':
    print(f'O valor {num} em Binário é {bin(num)[2:]}')
elif opcao == '2':
    print(f'O valor {num} em Octal é {oct(num)[2:]}')
elif opcao == '3':
    print(f'O valor {num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('OPÇÃO INVALIDA!') '''







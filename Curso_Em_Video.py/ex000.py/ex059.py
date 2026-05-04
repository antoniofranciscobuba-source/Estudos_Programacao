'''
Cria um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números 
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

maior = 0
opcao = 0
while opcao != 5:
    print('''OPÇÕES:
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'{n1} X {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior número é {maior}')
    elif opcao == 4:
        print('INSIRA NOVOS NÚMEROS')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
    
    
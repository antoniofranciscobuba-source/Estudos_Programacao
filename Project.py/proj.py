from time import sleep 
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

maior = 0
opcao = 0
while opcao != 5:
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números 
        [5] Sair do programa''')
    opcao = int(input('>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f' {n1} + {n2} = {soma}')
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
        n1 = int(input('Digita um valor: '))
        n2 = int(input('Digita outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Erro! Por favor, tente novamente!')
print('Volte sempre...')
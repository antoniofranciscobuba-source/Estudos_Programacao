'''
Crie um programa que simule o funcionamento de um caixa eletrônio. No inicio 
pregunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues:
OBS: Considere que o caixa possui cédulas de: €50, €20, €10 e €1.
'''
print(f'{' BANCO JC ':=^20}')
valor = int(input('Qual valor você quer sacar? €'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de €{céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO JC! Tenha um bom dia!')

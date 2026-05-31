'''
Elabore um programa que calcule o valor a ser pago
por um produto considerando o seu preço normal e 
condição de pagamento:

- À vista dinheiro/ cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até duas 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros.
'''
print(f'{'LOJA JILSON':=^40}')
preco = float(input('Preço do produto: €'))
print('''FORMAS DE PAGAMENTO:
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2X no cartão
      [4] 3X ou mais no cartão''')
opcao = input('Qual é a opção? ')

if opcao == '1':
    total = preco - (preco * 10 / 100)
elif opcao == '2':
    total = preco - (preco * 5 / 100)
elif opcao == '3':
    total = preco
    parcela = total / 2
elif opcao == '4':
    total = preco + (preco * 20 / 100)
    totaparc = int(input('Quantas parcelas? '))
    parcela = total / totaparc
    print(f'Sua conta será parcelada em {totaparc} X de €{parcela:.2f} COM JUROS.')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de €{preco:.2f} vai custar €{total:.2f} no final')


"""
Faça uma algoritimo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.
"""
preço = float(input('Digite o preço €: '))
novo_preço = preço - (preço * 5 / 100)
print(f'O preço do produto é {preço}€ com o desconto de 5% será: {novo_preço:.2f}€')
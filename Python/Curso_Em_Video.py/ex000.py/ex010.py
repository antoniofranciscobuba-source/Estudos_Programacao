""""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dolares ela pode comprar considera: USS1.00

"""
# Para converter Euro
euro = float(input('Quanto dinheiro você tem na carteira? '))
dolar = euro * 1.19
print(f'Você pode comprar {dolar:.2f}$')

 # Para converter reias
real = float(input('Quanto dinheiro você tem na conta? '))
dolar = real / 5.23
print(f'Você pode comprar: {dolar:.2f}R$')

# Para kwanza
kwanza = float(input('Quanto dinheiro você tem na conta? Kz: '))
dolar = kwanza / 917
print(f'Com {kwanza:.2f}Kz, você pode comprar: {dolar:.2f}$')


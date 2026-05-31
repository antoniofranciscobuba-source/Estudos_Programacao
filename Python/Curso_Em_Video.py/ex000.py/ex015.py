"""
Ecreva um programa que pergunta a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos que ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 pr Km rodado.
"""
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias? '))
pagar = (km * 0.15) + (dias * 60)
print(f'O preço total a pagar é {pagar:.2f}R$')



'''
Ecreva um programa que leia a velocidade de um carro.

Se ele eltrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,0 Reias para cada
Km acima do limite.
'''

v = float(input('Qual é a velocidade do carro (Km): '))
m = (v - 80) * 7.0

if v >= 80:
    print(f'Você foi multado por andar a {v}Km/h e vai ter que pagar, R${m:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
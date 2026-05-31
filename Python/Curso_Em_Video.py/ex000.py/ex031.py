'''
Desenvolva um programa que pergunta a distancia de uma 
viagem em Km.
calcule o preço da passagem cobrando R$ 0,50 por Km
para viagem até 200Km e R$0,45 para viagens mais longas.
'''
'''
distancia = float(input('Digite a distancia em Km: '))

if distancia <= 200:
    print(f'Você viajará {distancia:.1f}Km, isso custa: R${distancia * 0.50:.2f}')
else:
    print(f'Você viajará {distancia:.1f}Km, isso custa: R${distancia * 0.45:.2f}')
'''

distancia = float(input('Digite uma distancia em Km: '))
di = 0.50 * distancia if distancia <= 200 else 0.45 * distancia
print(f'Voce viajará {distancia:.1f}Km, isso custará: R${di:.2f} ')


    

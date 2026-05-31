"""
 Faça um programa que leia a largura e a altura de uma parede em metros, 
 calcule a sua area e quantidade 
 de tinta nessessaria para pinta-la, sabendo que cada litro de tinta
 pinta uma área de 2**(1/2) m².
 """

altura = float(input('Digite a altura (m): '))
largura = float(input('Digite a largura (m): '))
area = altura * largura
tinta = area / 2

print(f'Sua parede tem a dimensão de {altura} X {largura} e a sua area é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta') 
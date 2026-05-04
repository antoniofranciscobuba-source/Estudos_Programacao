"""
Faça uma algoritimo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""

salário = float(input('Digite o salário:€ '))
novo_salário = salário + (salário * 15 / 100)
print(f'Seu salário era {salário:.2f}€, com aumento de 15% passará para: {novo_salário:.2f}€')

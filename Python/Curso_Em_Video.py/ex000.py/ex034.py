'''
Faça um programa que leia o saário de um funcionario
e calcule o valor do seu aumento

para salarios superiores a R$1.250.00 
calcule um aumento de 10%.

para os inferiores ou ingual,
o aumento é de 15%.
'''
from time import sleep
salario = float(input('Qual é o seu salário? R$ '))

cores = {'limpa': '\033[m',
         'azul': '\033[4;36;40m',
         'roxo': '\033[35;40m'}
print('-' * 13)
print(f'{cores["roxo"]}ANALIZANDO...{cores["limpa"]}')
print('-' * 13)
sleep(1.5)
if salario > 1250:
   aumento = (salario * 10) / 100
else:
   aumento = (salario * 15) / 100
print(f'{cores["azul"]}Salario atual R${salario:.2f} com o seu aumento passa para R${salario + aumento:.2f}{cores["limpa"]}')




'''
if salario > 1250.00:
   print(f'Você tem o aumento de 10% R${(salario * 10) / 100:.2f} + o salário atual isso da: R${((salario*10) /100) + salario:.2f}')
else:
   print(f'Você ganhou aumento de 15% R${(salario * 15) / 100:.2f} + salário atual isso da: R${((salario*15)/100) + salario:.2f}')
'''
   

'''
Desenvolva uma logica que leia o peso e altura da pessoa, calcule seu IMC,
e mostre statu, de acordo com a tabela abaixo.

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobre peso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'O seu IMC é {imc:.2f} ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print(f'O seu IMC é {imc:.2f} PESO IDEAL')
elif 25 <= imc <= 30:
    print(f'O seu IMC é {imc:.2f} SOBREPESO')
elif 30 <= imc <= 40:
    print(f'O seu IMC é {imc:.2f} OBESIDADE')
else:
    print(f'O seu IMC é {imc:.2f} OBESIDADE MÓRBIDA')
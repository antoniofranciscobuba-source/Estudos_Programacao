name = str(input('Qual é o seu nome? '))
if name == 'Jilson':
    print('Que lindo nome')
else:
    print('Que nome estranho!')
print(f'Bom dia, {name}')

n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('PARABENS' if media >= 6 else 'ESTUDE MAIS')

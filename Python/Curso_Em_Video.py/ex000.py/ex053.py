'''
Cria um programa que leia um número qualquer e diga se ela é
um palíndromo, desconsiderando os espaços.
'''
'''
n = input('Digite um valor: ').strip().lower()
text = n[::-1]
if n == text:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
'''
n = input('Digite uma frase: ').upper()

n1 = n.replace(" ", " ")
c = n1[::-1]
if n == c:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')

#Também podemos fazer desse jeito.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  #Serve para fatiar a palavra
junto = ''.join(palavras) #Serve para juntar o fatiamento ou juntar as palavras
inverso = junto[::-1]  #[::-1] Serve para inverter a frase 
print(f'{junto} é {inverso}')
if inverso == junto:
    print('Temos um Palíndromo')
else: 
    print('A frase digitada não é Palíndromo')
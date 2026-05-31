"""
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos
import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar 
vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, 
oferecidos no Pypi.
"""

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a: {raiz:.2f}')

# Aqui a gente pode utilizar o from

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) 
print(f'A raiz de {num} é igual a: {raiz:.2f} ') 

# Outro esquema para random
import random
num = random.randint(4, 15)
print(num)

# escreva import e precione Ctrl e o botão espaço
# Para instalar modulos faça isso: abra um novo terminal e escreva: pip install === e a coisa que queres inst
import emoji
print(emoji.emojize("Teste: :check_mark_button:"))
print(emoji.emojize("Instalação concluída com sucesso! :rocket:"))
print(emoji.emojize("Rumo ao nível Sênior na França! :France: :laptop:"))
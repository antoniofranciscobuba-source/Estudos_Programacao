'''
Cria um programa que tenha uma tupla com vária palavras (Não usar acentos).
Depois disso você deve mostrar, para cada palavras quais são as suas vogais.
'''
palavras = ('banana', 'luanda', 'vai', 'nao', 'volte', 'sozinho', 'solta',
            'montanha', 'carroceu', 'esqueceu', 'enloqueceu', 'manha', 'nada',
            'italia', 'carrinho', 'vassoura', 'casa', 'cana', 'varinha', 'fica', 'amora')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''
Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a explressão passada com os parênteses aberto
e fechados na ordem correta.
'''
pilha = []
exp = input('Digite uma expressão: ')
for caracter in exp:
    if caracter == '(':
        pilha.append('(')
    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta✅')
else:
    print('A expressão está incorreta❌')
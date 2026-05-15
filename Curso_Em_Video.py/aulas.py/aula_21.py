'''def contador(i, f, p):
    """
    Faz uma contagem e mostre na tela.
    :Param i: inicio de contagem 
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    funcao criada pelo Jilson Lin.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')
help(contador)'''
'''
def soma(a=0, b=0, c=0):
    """
    Faz uma soma de tres valores e mostre o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    funcao criada pelo Jilson Lin.
    """

    s = a + b + c
    return s
r1 = soma(3, 2, 5)
r2 = soma(3, 6)
r3 = soma(4, 2)
print(f'Os resultados foram {r1}, {r2} e {r3}.')
help(soma)'''

'''
def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''
'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}.')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if par(num):
    print('é par')
else:
    print('nao é par')


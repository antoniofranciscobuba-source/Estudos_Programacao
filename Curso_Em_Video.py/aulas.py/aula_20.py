def mensagem(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)

#Programa principal
mensagem('Jilson Lin é um bom aluno')
mensagem('Margarida Buba é bem comportada')
mensagem('Dionisia é uma boa garota')
mensagem('Emma é uma boa amiga também')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('-' * 30)

#Programa Principal
soma(4, 5)
soma(5, 7)
soma(12, 5)

def calc(*num):
    print(f'Na casa de {num} deu {len(num)} ao todo')

calc(1, 2, 3, 4, 5,)
calc(3, 4, 5)
calc(1, 4, 4, 5)

def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [5, 3, 2, 6, 2, 1,]
dobro(valores)
print(valores)
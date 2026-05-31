# Crie um algoritimo que leia uma número e mostre o seu dobro, triploe a raiz Quadrada.
n1 = int(input('Digite um número: '))
print(f'Se o valor for {n1}, o dobro será: {n1*2},\n o triplo será: {n1*3}\n e a raiz quadrada será {pow(n1,(1/2)):.2f}')

# A gente tambem pode fazer desse jeito
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'Se o valor for: {n}.')
print(f'O dobro será: {d}.')
print(f'O triplo será: {t}.')
print(f'E a raiz quadrada será: {r:.2f}.')
#LISTAS

num = [5, 6, 7, 3, 4, 2]
num[1] = 2 #Para mudar o número ou muta-la, porque laços são mutáveis
num.append(9) #Para acrescentar mais um número 
num.sort(reverse = True) #para inverter a ordem
num.insert(2, 2)  #para acrescentar um número e qualquer lugar
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
#Parte 2 dos exemplos 
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(1, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!
print('Cheguei ao final da lista')'''
#parte 3 dos exemplos
'''
a = [1, 4, 5, 6, 3, 7]
b = a[:] #Isso cria uma cópia (Muito importante)
b[4] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

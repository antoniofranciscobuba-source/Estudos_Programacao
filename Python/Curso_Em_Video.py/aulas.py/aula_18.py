
dados = []
pessoas = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar: ')).strip().upper()[0]
    if resp == 'N':
        break
print(pessoas)
'''
pessoas = [['Pedro', 34], ['Maria', 25], ['Samanta', 33]]  #Lista dentro da lista
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[1])'''

'''
teste = []
teste.append('Jilson')
teste.append(30)
galera = []
galera.append(teste[:]) #Nunca esquecer os parentes para fazer a copia
teste[0] = 'António'
teste[1] = 25
galera.append(teste[:])
print(galera)'''

'''
galera = [['Paulo', 33], ['Maria', 23], ['Ana', 45], ['Domingos', 17]]
galera.sort()
galera.sort(reverse=True)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
'''
dado = []
galera = []
totmai = totmen = 0
for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('-=' * 20)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.') '''
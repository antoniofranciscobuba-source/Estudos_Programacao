'''
Um professor quer sortear um dos seus quatros alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
name1 = str(input('Primeiro aluno: '))
name2 = str(input('Segundo aluno: '))
name3 = str(input('Treiceiro aluno: '))
name4 = str(input('Quarto aluno: '))
lista = [name1, name2, name3, name4]
sorteio = random.choice(lista)
print(f'O sorteio do aluno foi: {sorteio}')

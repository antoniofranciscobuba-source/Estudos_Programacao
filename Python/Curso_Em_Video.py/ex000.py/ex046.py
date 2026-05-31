'''
Faça um programa que mostre na tela uma contagem regreassiva
para o estouro de fuguetes de artificios, indo de 10 até a 0
com uma pausa de um segundo entre elas.
'''
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('✨✨✨FELIZ ANO NOVO🎉🎉🎉...')
'''
Desenvolva um programa que leia o comprimento 
de três lados e diga para o usuário se ele
pode ou náo formar um triâgulo. r1, r2, r3.

'''
from time import sleep

r1 = float(input('Primeiro comprimento: '))
r2 = float(input('Segundo comprimento: '))
r3 = float(input('Treiceiro comprimento: '))

print('\033[0;34m*\033[m' * 13)
print('\033[0;36mANALISANDO...\033[m')
print('\033[0;34m*\033[m' * 13)
sleep(1.5)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima \033[4;36;40mPODEM FORMAR\033[0m um triangulo')
else:
    print('Os segmentos acima \033[4;31;40mNÃO PODEM FORMAR\033[0m um triangulo')




'''lanchi = ('Hanburguer', 'Suco', 'Tomate', 'manga')
#Para organizar a gente pode utilizar o sorted
#print(solted(lachi))
#print(lanchi)

for comida in lanchi:  #A gente pode utilizar essa forma
    print(f'Eu vou comer {comida}')

#for cont in range(0, len(lanchi)): #Essa é a segunda forma 
    #print(f'Eu vou comer {lanchi[cont]} na posição {cont}')

for pos, comida in enumerate(lanchi): #E essa é a treiceira forma 
    print(f'Eu vou comer {comida} na posição {pos}')
print('COMI PRA CARAMBA!')
'''
# A Tupla é imutável, por isso a gente não pode substituila nem apagala 
pessoa = ('Jilson', 19, 'M', 60.9)
del(pessoa)
print(pessoa)
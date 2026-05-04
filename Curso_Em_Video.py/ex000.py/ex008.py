# Escreva um programa leia um valor em metro e exiba convertido em centimetros e milimetros.

medida = float(input('Digite a medida: '))
cm =  medida * 100
mm = medida * 1000
print('A medida de {}m, corresponde a: {}cm, e {}mm'.format(medida, cm, mm))

#valor que exibe todas medidas
medida = float(input('Digite a medida: '))
km = medida / 1000  #Quilômetro >>> km
hm = medida / 100 #Hectômetro >>> hm
dam = medida / 10  #Decâmetro >>> dam
m = medida * 1  #Metro >>> m
dm = medida * 10  #Decímetro >>> dm
cm = medida * 100  #Centímetro >>> cm
mm = medida * 1000 #Milímetro >>> mm
print(f'O valor {medida} \n corresponde a: {km} km \n {hm} hm \n {dam} dam \n {m} m \n {dm} dm \n {cm} cm \n {mm} mm')
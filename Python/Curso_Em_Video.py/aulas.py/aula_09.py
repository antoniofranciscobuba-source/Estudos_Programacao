frase = 'Que Dia Mais Legal'

print(frase[:5]) #Para separar caracteres 

print(len(frase))  #Para contar quantos caracter tem

print(frase.count('a'))  #Para saber quantos caracctere da letra selectionada tem

print(frase.find('ga')) #Para verificar a letra digitada

print(' Legal' in frase)  #Para verificar se a letra se encontra na frase

print(frase.replace('Legal', 'fantastico')) #Para subistituir uma palavra da outra

print(frase.upper())  #Para colocar todas letras em Maiuscula

print(frase.lower())  #Para colocar todas letras em menuscula

print(frase.capitalize())  #Para colocar a primeira letra da primeira palavra em maiuscula

print(frase.title())  #Para colocar todas primeiras letras das primeiras palavras da frase em Maiuscula

print(frase.strip())   #Podes usar o frase.rstrip ou frase.lstript esquerda e direita

print(frase.split())  #Para separar ou para cortar as palavras 

print('-'.join(frase))  #Para adicionar '-' ou uma outra coisa em cada caracter depois de uma letra

print('''Não tenho nada a dizer agora, porque terei que pensar melhor 
      no teu caso. Por favor não se preocupe com isso
      O seu casso sera resolvido em breve, podes relaxar e se cuidar.
''')

'''
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel,
EX: escreva('Olá, Mundo!)
sída:
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''
def escreva(msg):
    tamanho = len(msg)
    tot = '~' * tamanho
    print(tot)
    print(msg)
    print(tot)
      
escreva('  LUA DE MEL  ')
escreva('UMA MARATONA INCRIVEL ')
escreva('COM FÉ A GENTE CONSEGUE MANTER A CALMA ')
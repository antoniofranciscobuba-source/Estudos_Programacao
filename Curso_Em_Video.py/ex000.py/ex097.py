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
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

      
escreva('LUA DE MEL')
escreva('UMA MARATONA INCRIVEL')
escreva('COM FÉ A GENTE CONSEGUE MANTER A CALMA')
escreva('A tecnologia tem evoluído muito nos ultimos tempos')
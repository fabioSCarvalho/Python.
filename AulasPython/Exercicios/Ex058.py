''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer. '''

from random import randint
from time import sleep

print('-=-' * 10)
print(' Vou sortear um numero, tente adivinhar!! ')
print('-=-' * 10)

print('\n Sorteando ...')
sleep(5)
sorteado = randint(0, 10)

n = int(input('Tente adivinhar o numero sorteando entre 0 e 10 :'))
tentativas = 1

while sorteado != n:
    print('Numero incorreto. Tente novamente')
    n = int(input('Tente adivinhar o numero sorteando entre 0 e 10 :'))
    tentativas += 1

print('-=-' * 10)
print('\n O numero sorteado foi {}. Parabéns, você ganhou'.format(n))
print('Numero de tentativas: {}'.format(tentativas))

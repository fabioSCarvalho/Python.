#Escreva um programa que faça o computador pensar em numero entre 0 e 5
#e peça para o  usuario tentar descobrir o numero escolhido
#o programa deverá escrever na tela se o usuario perdeu ou venceu

from random import randint
sorteado = randint(0,5)

print('-=-' * 10)
print('sorteando...')
print('-=-' * 10)

n = int(input('Tente adivinhar o numero sorteado entre 0 e 5 :'))

if n == sorteado:
    print('Você ganhou')
else:
    print('Você perdeu! O numero sorteado foi {}'.format(sorteado))

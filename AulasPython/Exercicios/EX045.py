# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random

jokenpo = ['Pedra', 'papel', 'tesoura']
jogada = random.randint(0, 2)

computador = jokenpo[jogada]
print(computador)
print('''Escolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesora''')

jogador = int(input('Qual sua escolha? '))
print("\n -=-=-=-=-=")
print("O computador escolheu {}".format(jokenpo[jogada]))

if jogada == 0:
    if jogador == 1:
        print("empatou")
    elif jogador == 2:
        print("Você ganhou")
    elif jogador == 3:
        print("Você perdeu")
    else:
        print("jogada inválida")
if jogada == 1:
    if jogador == 1:
        print("Você Perdeu")
    elif jogador == 2:
        print("Empatou")
    elif jogador == 3:
        print("Você ganhou")
if jogada == 2:
    if jogador == 1:
        print("Você ganhou")
    elif jogador == 2:
        print("Você perdeu")
    elif jogador == 3:
        print("Empatou")

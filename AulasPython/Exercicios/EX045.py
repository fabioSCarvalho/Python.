'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

import random

jokenpo = ['Pedra', 'papel', 'tesoura']
jogada = random.randint(0,2)

computador = jokenpo[jogada]
print(computador)
print('''Escolha sua jogada:
[1] Pedra
[2] Papel
[3] Tesora''')

opc = int(input('Qual sua ecolha? '))


 
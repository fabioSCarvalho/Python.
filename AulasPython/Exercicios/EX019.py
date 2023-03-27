#Um professor quer sortear um de seus quatro alunos para
# apagar o quadeo. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escollhido

from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aaluno: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))

lista = [nome1, nome2, nome3, nome4]

sorteado = choice(lista)


print('O alunno escolhido foi {}'.format(sorteado))


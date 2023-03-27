#Crie um programa que leia um numero real pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Dite um número: '))
intnum = trunc(num)

print('O numero {} tem a parte inteira {}'.format(num,intnum))







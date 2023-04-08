#Crie um programa que leia um número inteiro 
# e mostre na tela se ela é Par ou Impar.

numero = int(input('Infome um numero: '))

if numero % 2 == 0:
    print('{} é um numero par'. format(numero))
else:
    print('{} é um numero impar'.format(numero))
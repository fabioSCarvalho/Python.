# Escreva um programa que leia dois numero e diga 
# Qual dos dois é maior ou se são iguais 
n1 = int(input('Infomre o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))

if n1 > n2:
    print('O primeiro numero é maior')
elif n2 > n1 :
    print('O segundo numero é maior')
else:
    print('Os numero são iguais')

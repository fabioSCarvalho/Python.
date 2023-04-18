# Faça um programa que leia três numeros e
# mostre qual é o maior e qual é o menor.

n1 = int (input('Primeiro numero: '))
n2 = int (input('Segundo numero: '))
n3 = int (input('Terceiro numero: '))

maior = n1
menor = n2

    
if n2 > n1 and n2 > n1:
    maior = n2
if n3 > n1 and n2 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3<n1:
    menor = n3

print('O numero {} é o maior'.format(maior))
print('O numero {} é o menor '.format(menor))

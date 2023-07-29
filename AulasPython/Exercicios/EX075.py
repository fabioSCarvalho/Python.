#Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input('Digite o primeiro valor')),int(input('Digite o primeiro valor')),int(input('Digite o primeiro valor')),int(input('Digite o primeiro valor')))

print(f'Você digitou {numeros}')
print(f'O numero 9 foi encontrado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu na {numeros.index(3)+1}° posição')
print(f'Os valores pares digitados foram ', end=" ")
for n in numeros:
    if n % 2 == 0:
        print(f'{n}',end=' ')


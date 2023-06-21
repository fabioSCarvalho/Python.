''' Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

media = 0
soma = 0
cont = 1

n = int(input('Digite um numero: '))
menor = n
maior = n
soma += n

opc = str(input('Quer continuar: [S][N]')).upper().strip()

while opc in 'Ss':
    n = int(input('Digite um numero: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    soma += n
    opc = str(input('\n Quer cntinuar: [S][N]')).upper().strip()

media = soma / cont

print('A media dos valores digitados é: {}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))


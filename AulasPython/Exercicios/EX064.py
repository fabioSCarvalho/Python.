''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''

n = int(input('Digite um numero [999 para parar]: '))
soma = 0
tot = 0
while n != 999:
    soma += n
    tot += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('\n Foram digitados {} numeros e a soma de todos os valores é {}'.format(tot, soma))

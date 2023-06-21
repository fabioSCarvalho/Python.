'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

num = 0

while True:
    if num < 0:
        break
    print('-=-=-' * 7)
    num = int(input('Digite um numero para ver sua tabuada '))
    print('-=-=-' * 7)
    for n in range(0, 11):
        print(f'{num} X {n} = {num * n}')
print('Programa finalizado')

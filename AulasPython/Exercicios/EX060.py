'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

n: int = int(input('Digite um numero para ver o seu fatorial: '))
fat = 1
while n > 0:
    print('{}'.format(n), end='')
    if n > 1:
        print(' X ', end='')
    else:
        print(' = ', end='')
    fat *= n
    n -= 1

print(' {}'.format(fat))

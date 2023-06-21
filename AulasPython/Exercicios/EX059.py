'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import  sleep
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0

while opc != 5:

    print('''  [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opc = int(input('\nDigite a opção desejada: '))

    if opc == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        sleep(2)
    elif opc == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
        sleep(2)
    elif opc == 3:
        if n1 > n2:
            print('O {} é o valor maior'.format(n1))
            sleep(2)
        elif n2 > n1:
            print('O {} é o valor maior'.format(n2))
            sleep(2)
        else:
            print('Os valores são iguais')
            sleep(2)
    elif opc == 4:
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('Digite o segundo valor: '))
        sleep(2)
    else:
        if opc > 5:
            print('Opção incorreta')
            sleep(2)
    print('-=-' * 15)
print('programa encerrado')

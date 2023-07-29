from random import randint
'''  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
cont = 0
while True:
    print('-=-' * 30)
    opc = str((input(' Par ou Impar [I/P]'))).upper().strip()
    n = int(input('Digite um numero: '))
    pc = randint(0, 10)
    soma = n + pc
    print(f' Você escolheu {opc} e jogou {n} \n o computador jogou {pc}')
    print(f'A soma foi {soma}')

    print('-='*30)

    if opc in 'Pp':
        if soma % 2 == 0:
            print('deu par, Você ganhou \n')
            cont += 1
        else:
            print('deu impar, você perdeu \n')
            break

    elif opc in 'Ii':
        if soma % 2 == 0:
            print(f' deu par, Você perdeu \n')
            break
        else:
            print('deu impar, Você ganhou \n')
            cont += 1
print('-=-' * 30)
print('Fim de jogo')
print(f' Você ganhou {cont} vezes')


''' perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''


termo = int(input('Digite primeiro termo para ver a PA: '))
razao = int(input('Informe a razao: '))
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('pause')
    mais = int(input('\n Quantos termos mais quer mostrar?'))

print('fim')

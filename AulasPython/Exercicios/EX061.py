'''  Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

termo = int(input('Digite um numero para ver a PA: '))
razao = int(input('Informe a razao: '))
cont = 0
while cont < 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('fim')

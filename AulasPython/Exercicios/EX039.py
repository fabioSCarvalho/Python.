#programa que leia o ano de nascimento e diga se deve se alistar

from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year 
idade = atual - nasc

print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual ))

if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade 
    print('Você ainda não tem 18 anos, falta {} anos para o alistamento'.format(saldo))
else:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
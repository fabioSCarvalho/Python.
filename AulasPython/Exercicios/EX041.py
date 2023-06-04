# leia o ano de nascimento e diga sua classificação

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Clasificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
    
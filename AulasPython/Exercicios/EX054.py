'''  Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade
  e quantas já são maiores. '''
from datetime import date

maior = 0
menor = 0
atual = date.today().year


for pessoa in range(0, 7):
    nasc = int((input('Em que ano a {}° pessoa nasceu? '.format(pessoa + 1))))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    print('-=' * 15)
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoas cadastradas são de maior'.format(maior))
print('{} pessoas cadastradas são de menor'.format(menor))

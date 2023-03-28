#Faça um exercicio que leia ma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ele aparece pela primeira vez 
#Em que posição ele aparece pela última vez

nome =str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A ukltima posição apareceu na posição {}'.format(nome.rfind('A')+1))
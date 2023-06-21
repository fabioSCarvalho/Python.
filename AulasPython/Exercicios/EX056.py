'''  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

totIdade = 0
nomeVelho = ''
idadeVelho = 0
idadeM = 0

for cadastro in range(1, 5):
    nome = input('Informe o nome da {}° pessoa: '.format(cadastro))
    idade = int(input('Informe a idade da {}° pessoa: '.format(cadastro)))
    sexo = input('Informe o sexo: [F] [M]: ').upper()
    print('=-' * 10)
    totIdade += idade

    if cadastro == 1 and sexo == 'M':
        idadeVelho = idade
        nomeVelho = nome
    else:
        if idade > idadeVelho and sexo == 'M':
            idadeVelho = idade
            nomeVelho = nome

    if sexo == 'F' and idade < 20:
        idadeM += 1

mediaIdade = totIdade / 4

print('A média de idade das pessoas cadastradas é: {} '.format(mediaIdade))
print('O nome Do homem mais velho cadastrado é {} e tem {} anos de idade'. format(nomeVelho, idadeVelho))
print('Foram cadastradas {} mulheres menores de 20 anos'.format(idadeM))


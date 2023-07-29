#  Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar 
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = 0
contHomem = 0
mulherMenor = 0
while True:

    print('--'*30)
    print(' \tCadatro\t')
    print('--'*30)

#recebendo os dados e validando se o sexo apenas se tiver M ou F
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()

 # contando os homens cadastrados. Se for do sexo masculino o contador 'contHomem' recebe mais um 
    if sexo in 'Mm':
        contHomem += 1

 #Contando quantas pessoas são maiores de 18. Se for maior de 18 o contador 'maior' recebe mais um   
    if idade > 18:
        maior += 1

#contando quantas mulheres menores de 20 foram cadastradas. Se for menor que 20 o contador 'mulhermenor' recebe mais um    
    if idade < 20 and sexo in 'Ff':
        mulherMenor += 1

 #Verifica se quer cadastrar mais pessoas   
    print('--'*30)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N]')).upper().strip()
    if opc in 'Nn':
        break

print(f' Foram cadastradas {contHomem} homens')
print(f' {maior} pessoas eram maior de 18')
print(f' Das mulheres cadastradas {mulherMenor} tinham menos de 20 anos de idade')



''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input('digite o sexo [M][F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = input('Dado inválido, informe o sexo [M][F]: ').strip().upper()
print('Registrado com sucesso')

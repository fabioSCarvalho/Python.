#Crie um programa que leia o nome de uma pessoa 
# e diga se ela tem "SILVA NO NOME"

nome = str(input('Nome completo: ')).strip().upper()

print('Seu nome tem Silva: {}'.format('SILVA' in nome))
# Crie um programa que leia o nome e o preço de
# vários produtos. O programa deverá perguntar se
# O usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
total = 0
menor = 0
mil  =  0
cont = 0 
nome = ''

while True:
    
    print('--' * 30)
    print('\t Lojão \t')
    print('--' * 30)

#Recebendo os dados nescess
# ários 
    produto = str(input('Informe o nome do produto: ')).split()
    valor = float(input('Informe o preco: R$ '))
    cont += 1

# Verificando o produto mais barato
    if cont == 1 or valor < menor:
        menor = valor
        nome = produto

#Somando o total da compra e armazenado na variavel total
    total += valor

#Contando os produtos que custam mais de mil
    if valor > 1000:
        mil += 1
    
#Validando se que continuar, apenas recebendo S ou N. caso N dar um break
    opc = ' '
    while opc not in 'SN':
        opc = input('Gostaria de continuar: [S/N] ').upper().strip()
    if opc in 'nN':
        print('--' * 35)
        break

print(f'\n O total da sua compra foi R$ {total:.2f}')
print(f' Foi comprado {mil} produtos custando mais de mil')
print(f'O produto mais barato comprado foi {nome}, custando {menor:.2f}')

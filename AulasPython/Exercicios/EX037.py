# Crie um programa que leia um numero iteiro qualquer 
# e peça para o usuario escolher qual será a base de conversão:
# Binario, octal, Hexadecimal

n = int(input('Digite um numero inteiro: '))

print('''Escolha a uma das bases para a conversão:
[1] Converter para binario
[2] Converter para octal
[3]Converter para HExadecimal''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binario é {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opcao invalida')
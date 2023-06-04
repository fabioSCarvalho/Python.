# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

num = int(input("Digite um numero: "))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print("\033[33m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print('{}'.format(n), end=' ')
if tot == 2:
    print("\n O numero {} é primo".format(num))
else:
    print("\n O numero {} não é primo".format(num))
print("\n \033[m o  {} foi dividido {} vezes ".format(num, tot))


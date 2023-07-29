print(5+2) #soma
print(5-2) #subtração
print(5*2) #multiplicação
print(5/2) #Divição
print(5**2) #potencia
print(5//2) #Divição inteira
print(5%2) #Resto da divisão

n1 = str(input('Qual seu nome: '))
print('prazer {:=^20}'.format(n1))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('primeiro valor é {} e \n o segundo valor é {} '.format(n1, n2))
print('A soma é {}: '.format(s), end=' ')
print('A multiplicação é : {}'.format(m))
print('a Divisão é: {:.2f}'.format(d))
print('A divisão inteira: {}'.format(di))
print('A potencia é: {}'.format(e))





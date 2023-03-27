#Faça um programa que converta real em dólar. Considerando o dolar 3,27
dinheiro=float(input('Quanto dinheiro você tem na carteira:  R$'))
dolar = dinheiro / 3.27
print('Com R$ {} você pode comrar US${:.2f}'.format(dinheiro, dolar))


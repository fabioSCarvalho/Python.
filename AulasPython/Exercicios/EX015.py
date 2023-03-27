# Escreva um programa que pergunte a quantidade de km percorrida por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias = int(input('Informe por quantos dias você alugou: '))
Km = float(input('Informe quantos km você percorreu: '))

precoapagar = (60 * dias) + (Km * 0.15)

print('o total a pagar é de R${:.2f}'.format(precoapagar))



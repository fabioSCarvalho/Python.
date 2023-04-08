#DEsenvolva um programa que pergunte a distancia de uma viagem km
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km
# e R$0.45 para viagens maislongas

dist = str(input('Informe a distancia da viagem : Km ')).strip() 

distancia = float(dist)

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('Com {}Km de distacia o valor total da passagem é de R${:.2f}'.format(distancia, valor))
#Faça um programa que leia ao preço de um produto e mostre o seu preço com 5% de desconto
produto = float(input('Qual o preço do produto: R$'))
NovoValor = produto - (produto * 0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, NovoValor))

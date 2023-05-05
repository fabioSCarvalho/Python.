'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preco = float (input('Qual preço da sua compra : R$'))

print('''Formas de pagamantos:
      [1] á vista dinheiro/cheque
      [2] á vista no cartão
      [3] 2x no cartão
      [4] 3x Ou mais no cartão''')
opc = int(input('Qual opção: '))

if opc ==1:
    novopreco = preco - (preco * 10 / 100)
    print('Com desconto de 10% você pagará R${:.2f}'.format(novopreco))
elif opc == 2:
    novopreco = preco - (preco * 5 / 100)
    print('Com desconto de 5% você pagará R${:.2f}'.format(novopreco))
elif opc == 3:
     print('Você não teve desconto, o valor continuará R${:.2f}'.format(preco))
elif opc == 4:
     
     novopreco = preco + (preco * 20 / 100)
     parcela = int(input('Quantas parcelas: '))
     print('Sua compra parcelada em {}x de R${:.2f}'.format(parcela, novopreco / parcela))
     print('Com juros de 20%, pagará R${:.2f}'.format(novopreco))
else:
    print('Forma de pagamento incorreta')

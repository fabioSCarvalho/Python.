# Escreva um programa para aprovar o empréstimo bancário Prara comprar uma casa  #
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# A prestação mensal não pode ficar exceder 30% do salário 
# ou o empréstimo é negado.

salario = float(input (' Informe seu salário: R$'))
valor_casa = float (input ('Informe o valor da casa: R$'))
anos_parcela = int(input('Em quantos anos você deseja parcelar: '))

prestacao = valor_casa / (anos_parcela * 12)
porcento = salario * 30 / 100 

print('Valor da casa : R${:.2f}'.format(valor_casa))
print('Valor da prestação em {} anos: R${:.2f}'.format(anos_parcela, prestacao))

if prestacao > porcento:
 print ('empréstimo negado !! O valor da prestação excede 30% do seu salário')
else:
    print ('Emprestimo aprovado')
    
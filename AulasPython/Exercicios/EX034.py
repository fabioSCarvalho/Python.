# Escreva um mprograma que pergunte o salario do funcionario
# e calcule o valor do seu aumento:
#  Para salario superiores a 1.250,00 calcule um aumento de 10% 
#  Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('infome o seu salario : R$'))
salario_aumento = float

if salario <= 1250:
    salario_aumento = salario + (salario * 15 / 100) 
    print(' Com aumento de 15% seu salario de R${:.2f} ficará R${:.2f} '.format(salario, salario_aumento))
else:
    salario_aumento = salario + (salario * 10 / 100) 
    print(' Com aumento de 10% seu salario de R${:.2f} ficará R${:.2f} '.format(salario, salario_aumento))



# Temos uma tabela de produtos e serviços. com o aumento de imposto sobre serviçoes temos que atualizar 
# o opreço dos produtos e serviçoes impactados pela mudança

#novo multiplicadoor de imposto 1.5

#--------Usando Pandas---------------
import pandas as pd 

tabela1 = pd.read_excel('Analise tabela produto\Produtos.xlsx')
print(tabela1)

print('=-' * 50)
print('atualizar o multiplcador')
#atualizar o multiplcador
tabela1.loc[tabela1['Tipo'] == 'Serviço', 'Multiplicador Imposto'] = 1.5
print(tabela1)


print('=-' * 50)
print('Fazer a conta do preço base reais')
#Fazer a conta do preço base reais
tabela1['Preço Base Reais'] = tabela1['Multiplicador Imposto'] * tabela1['Preço Base Original']
print(tabela1)

#Salvar em um arquivo excel
#Colocando o mesmo nome do arquivo original, o python substitui 
tabela1.to_excel('Analise tabela produto\ProdutoPandas.xlsx', index=False)




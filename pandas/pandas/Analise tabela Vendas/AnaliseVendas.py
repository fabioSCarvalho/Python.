# analisando o faturamento das lojas
# Verificando qual tem mais vendas
# Descobrinfo o motivo dela ter mais vendas

from sys import displayhook
import pandas as pd
tabela = pd.read_excel('Vendas.xlsx')

displayhook(tabela)
'''
#pegar um panorama geral da empresa
print()
print('-=' * 10)
print('Fatutaramento total')
faturamento_total = tabela['Valor Final'].sum()
print(faturamento_total)

#Analise top ->down
#faturamento por loja
print()
print('-=' * 10)
print('Fatutaramento por loja')
faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento_por_loja)


#entrar no detalhe para entender
faturamento_por_produto = tabela [['ID Loja','Produto','Valor Final']].groupby(['ID Loja','Produto']).sum()
print(faturamento_por_produto)'''

id_loja = tabela[['ID Loja']]
print(id_loja)

# Analisando o resultado, percebesse que em uma das lojas tem um produto que as outras não tem

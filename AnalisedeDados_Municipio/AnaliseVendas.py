import pandas as pd
from displayfunction import display

''' Trazendo a base de dados para o python e ver o que tem nela '''
tabela = pd.read_excel('Vendas.xlsx')
print(tabela)


print('-=' * 30)
''' pegar um panorama geral da base de dados'''
#pegando o faturamento somando a coluna valor final
faturamento_total = tabela['Valor Final'].sum()
print(f' \n Faturamento total: {faturamento_total}')


print('-=' * 30)
''' Começar a analise top -> down '''
#faturamento por loja
faturamento_por_Loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento_por_Loja)

print('-=' * 30)
'''Entrar nos detalhes para entender'''
#Desconbrindo o pq uma loja está com as vendas a frente das outras
faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()
print(faturamento_por_produto)

'''É possivel visualizar que o que fez uma das lojas vender mais que as outras, foi um produto que a mesma tem e as outras não'''
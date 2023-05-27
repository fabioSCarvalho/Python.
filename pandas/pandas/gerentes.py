import pandas as pd

vendas_df = pd.read_excel('Vendas.xlsx')

gerentes_df = pd.read_excel('Gerentes.xlsx')
print(gerentes_df)

# mesclar dois DataFrame, procurar informações de um em outro

vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)
import pandas as pd

#crias um dicionario com dados
# dataframe= pd.DataFrame()
venda ={ 'data':['15/02/2021', '16/02/2021'],
        'valor': [500,300],
        'produto': ['feijão', 'arroz'],
        'qtd':[50,70]
        }

#adicionando o dicionario a um dataframe
vendas_df = pd.DataFrame(venda)

#visualizando os dados
print(vendas_df)
#display(vendas_df)

print('-=-=' * 10)

#Recebe aqrquivo excel e transforma em um dataframe do pandas
vendas_df = pd.read_excel('Vendas.xlsx')
print(vendas_df)
print('-=-=' * 10)

#Resumo de visualização dedado simples e uteis 
print(vendas_df.head(10)) #mostra as cinco primeiras linhas, dentro do parentese do heafe coloca qunatas linhas deseja ver 

print('-=-=' * 10)

print(vendas_df.shape) # metodo shape mostra quantas linhas e quantas colunas tem na tabela 

print('-=-=' * 10)

print(vendas_df.describe()) #da uma visão geral 

print('-=-=' * 10)


#filtrando apenas a variavel produto com com o nome da coluna. Quando se pega uma unica coluna é uma serie 
produtos = vendas_df['Produto']
print(produtos)

print('-=-=' * 10)


produtos = vendas_df[['Produto', 'ID Loja']] #Filtrando mais de uma coluna
print(produtos)

print('-=-=' * 10)

#loc é usado para pegar linha com certa condição 
print(vendas_df.loc[1])   #pegar uma linha
print('-=-=' * 10)

print(vendas_df.loc[1:5])   #pegar uma linha 1 até linha 5
print('-=-=' * 10)


#pegar linhas que  correspondem a uma condição
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])

# pegar varias linhas e colunas usando o loc
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
print(vendas_norteshopping_df)


#pegar um valor especifico usando o loc
print(vendas_df.loc[1,'Produto'])

# Adiicionando itens

# a partir de uma coluna
vendas_df['comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)


# criar coluna com valor padrão
vendas_df.loc[:,"imposto"] = 0
print(vendas_df)

#adicionar linhas 

#vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")
#print(vendas_dez_df)

#vendas_df = vendas_df.append(vendas_dez_df)

print(vendas_df)

# excluir linhas e colunas 
vendas_df = vendas_df.drop('imposto', axis=1)
print(vendas_df)


#valores vazios

#deletar linas e colunas vazias
vendas_df = vendas_df.dropna(how='all', axis=1)

# deletar linhas que possuem pelo menos um valor vazio
vendas_df = vendas_df.dropna()

#preencher valores vazios
#preencher com a média da coluna
vendas_df['comissão'] = vendas_df['comissão'].fillna(vendas_df['comissão'].mean())
print(vendas_df)

#preencher com o ultimo valor, valor acimas
vendas_df = vendas_df.ffill()

# metodos para calcular indicador
# Groupby
#Value Counts

#Quantas transações eu tive em cada loja 
transação_loja= vendas_df['ID Loja'].value_counts()
print(transação_loja)

#agruppar informações
#faturamento de cada produto
faturamento_produto = vendas_df[['Produto', 'Valor final']].groupby('Produto').sum() 
print(faturamento_produto)
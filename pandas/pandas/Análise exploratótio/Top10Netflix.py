import pandas as pd
import datetime as dt
base = pd.read_csv('netflix daily top 10.csv')

print(base)

print('As cinco primeiras')
base.head(5)


print('As cinco ultimas')
base.tail(5)


print('O tamanho da base')
base.shape()


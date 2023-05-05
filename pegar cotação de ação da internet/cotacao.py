from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

cotacao_bovvespa = web.DataReader('^BVSP', data_source='yahoo', start="01/01/2023", end="04/15/2023")
print(cotacao_bovvespa)


cotacao_bovvespa['Adj Close'].plot()
plt.show
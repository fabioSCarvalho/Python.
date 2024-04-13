import os
import pandas as pd
import win32com.client as win32
from datetime import datetime

caminho = 'C:/Users/win10/Documents/GitHub/Python/ProjetoFreela/bases'
arquivos = os.listdir(caminho)
print(arquivos)

tabela_consolidada = pd.DataFrame()


for nome_arquivo in arquivos:
    tabela_venda = pd.read_csv(os.path.join(caminho, nome_arquivo))
    tabela_venda["Data de Venda"] = pd.to_datetime("01/01/1900") + pd.to_timedelta(tabela_venda["Data de Venda"], unit="d")
    tabela_consolidada = pd.concat([tabela_consolidada, tabela_venda])
    
tabela_consolidada = tabela_consolidada.sort_values(by ="Data de Venda")
tabela_consolidada = tabela_consolidada.reset_index(drop=True)
tabela_consolidada.to_excel("Vendas.xlsx", index=False)


outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.to = 'fabiodesouza733@gmail.com'
data = datetime.today().strftime("%d/%m/%Y")
email.Subject = f"Relatório de venda {data}"
email.body = f"""
Prezados segue relatório de vendas de {data} atualizado.
attt
Fábio
"""
caminho_anexo = os.getcwd()
anexo = os.path.join(caminho_anexo, "Vendas.xlsx")
email.Attachments.Add(anexo)

email.Send()

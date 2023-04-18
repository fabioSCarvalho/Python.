import pandas as pd
from datetime  import date
from datetime import datetime as dt
cadastro = int(input('Infomre quantos alunos deseja cadastrar: '))
NomeAlunos = []
SerieAluno = int= []
contAlunos = 0

while contAlunos < cadastro:
    NomeAlunos.append(input(f'Infomre o nome do aluno {contAlunos}: '))
    contAlunos = contAlunos + 1

contAlunos = 0
while contAlunos < cadastro:
    SerieAluno.append(input(f'Infomre a serie do aluno {contAlunos}: '))
    contAlunos = contAlunos + 1

nome_df = pd.DataFrame(NomeAlunos, columns=['Nomes'])

print('=-' * 20)

Escola_df = nome_df
print(Escola_df)

print('=-' * 20)

Escola_df['Serie'] = SerieAluno
print(Escola_df)

print('=-' * 20)

data_hoje = date.today()
Escola_df['Data'] = data_hoje
print(Escola_df)

print('=-' * 20)


Escola_df['Data'] = Escola_df['Data'].astype('datetime64[ns]')
print(Escola_df)

print('=-' * 20)

Escola_df = Escola_df.sort_values(by='Serie', ascending=True, inplace=True)
print(Escola_df)








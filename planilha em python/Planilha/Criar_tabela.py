import openpyxl

nome_tabela = str(input('Informe o nome da  tabela: ')).strip()


book = openpyxl.Workbook()
book.create_sheet(nome_tabela)


tabela_page = book[nome_tabela]

tabela_page.append(['aluno'])

book.save('{}.xlsx'.format(nome_tabela)) 
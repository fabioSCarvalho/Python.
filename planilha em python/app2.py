import openpyxl

#Carregando um aquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

#Selecionando uma pagina 
frutas_page = book['Frutas']

#imprimindo os dadsode cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
   for cell in rows: 
  # #print(cell.value)
   # print(rows[0].value,rows[1].value,rows[2].value)

    if cell.value == 'Banana':
        cell.value = 'Frutas 1'

#Salvar alterções
book.save('Planilha de Compras v2.xlsx')
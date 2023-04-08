import openpyxl

#carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')

#selecinando uma pagina
frutas_page = book['Frutas']

#imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
   print({rows[0].value},{rows[1].value},{rows[2].value}) #imprimindo por linha
   
    #alterar um item da planilha
    #for cell in rows:
     #   if cell.value == 'Banana2':
      #      cell.value = 'melão'  
#salvar as alteraões em uma nova planilha
book.save('Planilha de compra v2.xlsx')

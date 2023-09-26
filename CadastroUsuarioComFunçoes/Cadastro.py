from FuncaoCadastro import *

usuario = ler_arquivo()

opc = chamaMenu()
if opc == 1:
    Cadastrar(usuario)
if opc == 2:
    importarjson()    
if opc == 4:
    Listar(usuario)
if opc == 5:
    Pesquisar()
if opc == 6:
    exportarJson()
if opc == 7:
    sair()

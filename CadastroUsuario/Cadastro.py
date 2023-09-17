from FuncaoCadastro import *

usuario = ler_arquivo()

opc = chamaMenu()
if opc == 1:
    Cadastrar(usuario)
print(usuario)
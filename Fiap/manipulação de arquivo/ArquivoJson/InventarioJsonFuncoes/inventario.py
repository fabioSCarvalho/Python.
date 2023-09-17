from Funcoesinventario import *

inventario = ler_arquivo("inventarioJson.json")

opcao = chamaMenu()

while opcao > 0 and opcao < 3:
    if opcao == 1:
        print(registrar(inventario,"inventarioJson.json"))
        gravarArquivo(inventario,"InventarioJson.json")
    elif opcao ==2:
        exibir("inventario_json.json")
    opcao = chamaMenu()

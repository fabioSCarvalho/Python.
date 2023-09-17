import json
import os
def chamaMenu():
    escolha =int(input('''Digite:
    [1] para registrar ativo
    [2] para exibir ativos armazenados'''))
    
    return escolha

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo_json:
            dicionario = json.load(arquivo_json)
    else:
        dicionario = {}

    return dicionario
    
def gravarArquivo(dicionario, arquivo):
    with open(arquivo, "w") as arquivo_json:
        json.dump(dicionario, arquivo_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o numero patrimonial: ")]=[input("Digite a data da ultima atualização: "), input("Digite a data da ultima atualização"), input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite [S] para continuar: ").upper()
    
    return "JSON gerado!!"

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])
import json
import os
from time import sleep

def chamaMenu():
    opc = int(input(''' 
        [1] Cadastrar usuario
        [2] Importar arquivo
        [3] Listar usuarios
        [4] Deletar usuarios
        [5] Pesquisar usuario
        [6] Exporar arquivo
        [7] Exit
    '''))

    return opc

def ler_arquivo():
    arquivo = "usuarios.json"
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo:
            usuarios = json.load(arquivo)
    else:
        usuarios = {}
    return usuarios

def Cadastrar(dicionario):
    opc = "S"
    email = []
    while opc == "S":   
        email.append(input("email: ").strip())
        opc = input("Deseja continuar: [S] [N]").upper()
        for email in email:
            print(email)
            dicionario[(email)]=[input("Nome: "), input("Setor: "), input("Cracha: ")]
    return dicionario
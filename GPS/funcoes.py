import os
import json

def endereco():
    endereco = {}
    endereco = {'endereco':[input('rua ou avenida: '),input('numero: '),input('cidade: ') ]}
    return endereco

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo) as arquivo_json:
            dicionario = json.load(arquivo_json)
    else:
        dicionario = {}
    return dicionario

def exportarJson(arquivo, dicionario):
    with open(arquivo, 'w') as arquivo_json:
            json.dump(dicionario, arquivo_json)

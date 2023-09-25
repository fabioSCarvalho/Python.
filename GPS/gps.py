import json
from funcoes import*
from geopy.geocoders import Nominatim

localizador = Nominatim(user_agent="GPS")

Tojson = endereco()

exportarJson('endereco.json', Tojson)

dicionario = ler_arquivo('endereco.json')

lista = dicionario['endereco']
endereco = lista[0]+ ', ' + lista[1] +  ' ' + lista[2]

localizacao = localizador.geocode(endereco)
localizado = str(localizacao).split(',')
print(localizado)
print(f'''Endereco: {localizado[0]}, {localizado[2]}, {localizado[3]},  {localizado[4]} 
    CEP: {localizado[-2]}''')

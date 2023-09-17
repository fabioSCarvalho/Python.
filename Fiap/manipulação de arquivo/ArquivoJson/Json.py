import json

usuario = {

"fabio@" : ["Fabio","Delivery","123"],
"eli@" : ["eliene","caixa","456"],
"ber@" : ["bernardo","creche","789"]
}

with open("bd1.json","w") as arquivo_json:
    json.dump(usuario,arquivo_json)

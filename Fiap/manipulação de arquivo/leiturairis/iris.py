basedados = []
with open("Python\Fiap\manipulação de arquivo\leiturairis\iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)
print(float(basedados[0][0]) + float(basedados[0][1]))


#criando arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("hakuna matata \n e lindo de ver \n hakuna  matata \n vai entenerr")


#Lendo cada linha do arquivo
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)

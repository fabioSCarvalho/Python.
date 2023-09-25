total = 0
Total2014 = 0
maiorTransito = 0
anoM = 0
mesM = 0
totalAno = 0
ano = input('Qual ano deseja pesquisar ')
media = 0
meidaMes = 0
with open("Python\maniulpaçãoArquivos\economic.csv", "r") as arquivo:
    for item  in arquivo.readlines()[1:-1]:
        total = total + float(item.split(",")[2])
        linha = item.split(",")

#Total de voos internacionais em 2014
        if linha[0] == '2014':
           Total2014 = Total2014 + float(linha[3])

#maior Transito no aero porto mes/ano      
        if(float(linha[3]) > float(maiorTransito)):
            maiorTransito = linha[2]
            anoM = linha[0]
            mesM = linha[1]
        
        if(float(linha[0]) == float(ano)):
            totalAno = totalAno + float(linha[2])

        if(float(linha[0]) == float(ano)):
            if(float(linha[5]) > float(media)):
                media = linha[5]
                meidaMes = linha[1]

print("--" * 50)
        
print(f"O total de voos é {total}")
print(f"O total de voos internacionais em 2014 foi {Total2014}")
print(f"O maior transito de passageiros ocorreu no mês {mesM} de {anoM}")
print(f" o mês que possui maior média diaria em um hotel em {ano} foi o mes {meidaMes} com {media}")
print("--" * 50)

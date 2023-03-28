#Crie um programa que leia o nome de uma cidade
#e diga se começa ou não com a palavra "SANTO"

cidade = str(input('Em que cidade você nasceu: ')).upper().strip()

print(cidade[:5] == 'SANTO') 
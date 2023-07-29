#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#  na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

time = ('Botafogo','Flamengo' ,'Grêmio','São Paulo','Fluminense','Palmeiras','Bragantino','Athletico-PR','Fortaleza','Cruzeiro',' Internacional','Atlético-MG','Cuiabá','Santos','Corinthians','Bahia','Goiás')

print(f'Os 5 primeiros colocados são: {time[:5]}')
print('-=' * 10)

print(f'Os quatro ultimos colocados são: {time[-4:]}')
print('-=' * 10)

print(f'Times em ordem alfabetica: {sorted(time)}')
print('-=' * 10)

print(f'O palmeiras está em {time.index("Palmeiras") + 1}° posição')
print('-=' * 10)
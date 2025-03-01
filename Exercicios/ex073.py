#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Vasco da Gama.

tabelaBrasileirao = ('Atletico-MG','Bahia','Botafogo','Ceara SC','Corinthians','Cruzeiro','Flamengo','Fluminense','Fortaleza','Gremio','Internacional','Juventude','Mirassol','Palmeiras','Bragantino','Santos','Sport Recife','Sao Paulo','Vasco da Gama','EC Vitoria')

for c in range(0,5):
    print(f'{c + 1}o - {tabelaBrasileirao[c]}\n')

for c in range(15,20):
    print(f'{c + 1}o - {tabelaBrasileirao[c]}\n')

print(sorted(tabelaBrasileirao))

print(f'O Vasco da Gama esta na {tabelaBrasileirao.index('Vasco da Gama') + 1}a colocacao')
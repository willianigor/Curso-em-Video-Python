#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint as rint
from operator import itemgetter

jogos = {
    'Jogador numero 1' : rint(1,6),
    'Jogador numero 2' : rint(1,6),
    'Jogador numero 3' : rint(1,6),
    'Jogador numero 4' : rint(1,6),
}

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("\nRanking dos jogadores:")
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"  {i}º lugar: {jogador} com {valor}")
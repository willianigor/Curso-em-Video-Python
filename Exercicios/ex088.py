#Exercício Python 088:
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

n_jogos = int(input('Quantos jogos voce quer sortear?\n'))

cont = 0
sorteios = list()
total_sorteios = list()

for a in range(n_jogos):
    for b in range(6):
        num = randint(1,60)
        sorteios.append(num)
    sorteios.sort()
    print(sorteios)
    total_sorteios.append(sorteios[:])
    sorteios.clear()
    sleep(0.5)

while True:
    opcao = str(input('Deseja exibir todos os jogos?(S/N)')).strip().upper()
    if opcao == 'S':
        print(total_sorteios)
    else:
        break




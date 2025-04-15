#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogadores = list()

while True:

    opcao = str(input('Deseja adicionar mais um jogador?(S/N)\n')).strip().upper()
    if opcao == 'N':
        break

    nome = str(input('Digite o nome do jogador:\n')).strip().title()
    n_partidas = int(input('Quantas partidas ele jogou?\n'))
    
    gols = list()
    saldo_gols = 0

    for c in range(n_partidas):
        n = int(input(f'Quantos gols ele fez na partida {c + 1}\n'))
        gols.append(n)
        saldo_gols += n

    aproveitamento = {
        'nome' : nome,
        'npartidas' : n_partidas,
        'gols' : gols.copy(),
        'saldo' : saldo_gols,
    }

    jogadores.append(aproveitamento)

for jogador in jogadores:
    print(f'Jogador {jogador['nome']}')
    print(f'  Numero de partidas: {jogador['npartidas']}')
    for i,g in enumerate(jogador['gols']):
        print(f'  {g} gol(s) na partida {i + 1}')
    print(f'  Saldo de gols: {jogador['saldo']}')

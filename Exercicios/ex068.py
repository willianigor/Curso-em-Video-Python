#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    numeroMaquina = randint(1,10)
    numeroUsuario = int(input('Digite um valor\n'))
    escolha = str(input('Voce quer PAR ou IMPAR?[P/I]\n')).strip().upper()
    while escolha not in ['P','I']:
            escolha = str(input('OPCAO INVALIDA!\nVoce quer PAR ou IMPAR?[P/I]\n')).strip().upper()
    if (numeroMaquina + numeroUsuario) % 2 == 0 and escolha == 'P':
        print(f'Voce escolheu {numeroUsuario} e a maquina {numeroMaquina}. Somando temos {numeroMaquina + numeroUsuario} que eh PAR\nPortanto VOCE GANHOU!')
        cont += 1
    elif (numeroMaquina + numeroUsuario) % 2 != 0 and escolha == 'I':
        print(f'Voce escolheu {numeroUsuario} e a maquina {numeroMaquina}. Somando temos {numeroMaquina + numeroUsuario} que eh IMPAR\nPortanto VOCE GANHOU!')
        cont += 1
    else:
        break
print(f'GAMER OVER!!\nVoce escolheu {numeroUsuario} e a maquina escolheu {numeroMaquina} que somados resultam em {numeroMaquina + numeroUsuario}\nVoce perdeu apos {cont} vitorias seguidas')

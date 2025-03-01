#O computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar
#Mostrando no final quantos palpites foram necessários para vencer.
from random import randint

numeroMaquina = randint(0,10)

print('Ola,sou seu computador!\nAcabei de pensar em numero entre 0 e 10.')

numeroUsuario = int(input('Tente adivinha-lo\n'))

cont = 1

while numeroUsuario not in [0,1,2,3,4,5,6,7,8,9,10]:
    numeroUsuario = int(input('Opcao invalida!!\nO numero que estou pensando esta compreendido entre 0 e 10\n'))

print(numeroMaquina)
while numeroMaquina != numeroUsuario:
    if numeroMaquina > numeroUsuario:
        numeroUsuario = int(input('ERROU!!\nO numero que estou pensando eh MAIOR que {}\n'.format(numeroUsuario)))
        cont += 1
    elif numeroMaquina < numeroUsuario:
        numeroUsuario = int(input('ERROU!!\nO numero que estou pensando eh MENOR que {}\n'.format(numeroUsuario)))
        cont += 1
print('Parabens!\nVoce acertou apos {} tentativas!\nO numero que eu estava pensando era mesmo o {}'.format(cont,numeroMaquina))

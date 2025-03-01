#Crie um programa que faça o computador jogar Jokenpô com você.
import random,time
print('VAMOS JOGAR JOKENPO!!')
print('''DIGITE O NUMERO DE ACORDO COM A TABELA!
1 ----- PEDRA
2 ----- PAPEL
3 ----- TESOURA\n''')
numeroMaquina = random.randint(1,3)
numeroUsuario = int(input('Ja escolhi o meu,agora escolha a sua jogada!\n'))

if numeroUsuario == 1 or numeroUsuario == 2 or numeroUsuario == 3:
    print('JO...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PO!!!!')
    if numeroUsuario == 1 and numeroMaquina == 1:
        print('USUARIO: PEDRA!!\nMAQUINA: PEDRA!!!')
        print('\033[1;33;43mEMPATE!\033[m\n')
    elif numeroUsuario == 2 and numeroMaquina == 2:
        print('USUARIO: PAPEL!!!!\nMAQUINA: PAPEL!!!')
        print('\033[1;33;43mEMPATE!\033[m\n')
    elif numeroUsuario == 3 and numeroMaquina == 3:
        print('USUARIO: TESOURA!!!!\nMAQUINA: TESOURA!!!')
        print('\033[1;33;43mEMPATE!\033[m\n')
    elif numeroUsuario == 1 and numeroMaquina == 2:
        print('USUARIO: PEDRA!!!!\nMAQUINA: PAPEL!!!')
        print('\033[1;31;41mUSUARIO PERDEU\033[m\n')
    elif numeroUsuario == 1 and numeroMaquina == 3:
        print('USUARIO: PEDRA!!!!\nMAQUINA: TESOURA!!!')
        print('\033[1;32;42mUSUARIO VENCEU!!\033[m\n')
    elif numeroUsuario == 2 and numeroMaquina == 1:
        print('USUARIO: PAPEL!!!!\nMAQUINA: PEDRA!!!')
        print('\033[1;32;42mUSUARIO VENCEU!!\033[m\n')
    elif numeroUsuario == 2 and numeroMaquina == 3:
        print('USUARIO: PAPEL!!!!\nMAQUINA: TESOURA!!!')
        print('\033[1;31;41mUSUARIO PERDEU\033[m\n')
    elif numeroUsuario == 3 and numeroMaquina == 1:
        print('USUARIO: TESOURA!!!!\nMAQUINA: PEDRA!!!')
        print('\033[1;31;41mUSUARIO PERDEU\033[m\n')
    elif numeroUsuario == 3 and numeroMaquina == 2:
        print('USUARIO: TESOURA!!!!\nMAQUINA: PAPEL!!!')
        print('\033[1;32;42mUSUARIO VENCEU!!\033[m\n')
else:
    print('\033[1;31;41mOPCAO INVALIDA!!\033[m\n')

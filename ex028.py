'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep

num1 = random.randint(0,5)
num2 = int(input('Tente adivinhar o numero que estou pensando,ele esta compreendido entre 0 e 5\n'))

print('PROCESSANDO...')
sleep(2)

if num2 == num1:
    print('Parabens,voce acertou,eu estava pensando no numero {} mesmo\n'.format(num1))
else:
    print('Voce errou,tente novamente.')
input('Pressione enter para sair.')

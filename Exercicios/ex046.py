#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
input('Aperte ENTER para iniciar a contagem regressiva')
for c in range(10,-1,-1):
    print(c)
    if c == 0:
        print('FELIZ ANO NOVO!!!')
    sleep(1)
input('Pressione ENTER para sair\n')
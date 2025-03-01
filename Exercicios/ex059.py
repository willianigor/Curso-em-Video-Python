#Crie um programa que leia dois valores e mostre um menu na tela:
#1 somar
#2 multiplicar
#3 dividir um pelo outro
#4 digitar novos numeros
#5 sair do programa
from time import sleep
n1 = float(input('Digite o primeiro numero\n'))
n2 = float(input('Digite o segundo valor\n'))
opcao = 1
   
while opcao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] DIGITAR NOVOS NUMEROS
[ 5 ] SAIR''')
    opcao = int(input('Digite a opcao desejada\n'))
    while opcao not in [1,2,3,4,5]:
        opcao = int(input('OPCAO INVALIDA\nDigite a opcao desejada\n'))
    if opcao == 1:
        print('A soma entre {} e {} equivale a {}'.format(n1,n2,n1 + n2))
        input('Pressione ENTER para continuar')
    elif opcao == 2:
        print('A multiplicacao entre {} e {} equivale a {}'.format(n1,n2,n1 * n2))
        input('Pressione ENTER para continuar')
    elif opcao == 3:
        if n1 > n2:
            print('{} eh o maior numero'.format(n1))
            input('Pressione ENTER para continuar')
        elif n1 < n2:
            print('{} eh o maior numero'.format(n2))
            input('Pressione ENTER para continuar')
        else:
            print('Voce digitou dois numeros iguais')
            input('Pressione ENTER para continuar')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro numero\n'))
        n2 = float(input('Digite o segundo valor\n'))
    else:
        print('FINALIZANDO...')
        sleep(1)
        break
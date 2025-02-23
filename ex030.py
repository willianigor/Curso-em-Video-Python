#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um numero inteiro\n'))

if n % 2 == 0:
    print('{} eh um numero PAR!\n'.format(n))
else:
    print('{} eh um numero IMPAR'.format(n))
print('Obrigado!')
input('Pressione ENTER para sair.\n')
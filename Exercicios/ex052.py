#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um numero\n'))
aux = 0

for c in range(1,numero + 1):
    if numero % c == 0:
        print('{} eh divisivel por {}'.format(numero,c))
        aux += 1
if aux != 2:
    print('Portanto,{} nao eh um numero primo\n'.format(numero))
else:
    print('{} eh um numero primo!Pois eh divisivel apenas por 1 e por ele mesmo.'.format(numero))
    
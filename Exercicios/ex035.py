#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Digite o valor para a primeira reta\n'))
r2 = float(input('Digite o valor para a segunda reta\n'))
r3 = float(input('Digite o valor para a terceira reta\n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {} e {} PODEM formar um triangulo!!'.format(r1,r2,r3))
else:
    print('NAO se pode formar um triangulo com as retas {}, {} e {}'.format(r1,r2,r3))
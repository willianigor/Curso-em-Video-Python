#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
n1 = n = int(input('Digite um numero para calcular seu fatorial\n'))

fatorial = 1

if n < 0:
    n = int(input('Impossivel calcular fatorial de numeros negativos!\nDigite um numero para calcular seu fatorial\n'))
else:
    while n > 1:
        fatorial *= n
        n -= 1
print('O fatorial de {} equivale a {}'.format(n1,fatorial))
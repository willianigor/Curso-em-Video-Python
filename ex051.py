#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
primeiroTermo = float(input('Digite o primeiro termo da PA\n'))
razao = float(input('Digite a razao da PA\n'))
soma = primeiroTermo

for c in range(10):
    soma += razao
    print('O termo de numero {} da sua PA equivale a: {:.2f}'.format(c + 1,soma))
    
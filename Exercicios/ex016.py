#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input('Digite um numero\n'))

print('A porcao inteira do numero {} vale {}'.format(num,math.trunc(num)))
print('A porcao inteira do numero {} vale {}'.format(num,int(num)))

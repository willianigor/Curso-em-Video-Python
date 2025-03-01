#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num1 = int(input('Digite um numero de 0 a 9999\n'))
num = str(num1)

print('O numero {} possui:\nO primeiro digito sendo o numero {}\nO segundo digito sendo {}\nO terceiro sendo {}\nE o quarto sendo {}\n'.format(num,num[0:1],num[1:2],num[2:3],num[3:4],num[3:]))

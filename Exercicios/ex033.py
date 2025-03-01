#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o NUMERO 1\n'))
n2 = float(input('Digite o NUMERO 2\n'))
n3 = float(input('Digite o NUMERO 3\n'))
menor = n1
maior = n1

if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

print('O MAIOR numero digitado foi: {}\nO MENOR numero digitado foi: {}'.format(maior,menor))


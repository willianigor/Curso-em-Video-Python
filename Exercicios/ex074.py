#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
menor = 11
maior = 0

for c in numeros:
    if c > maior:
        maior = c

for c in numeros:
    if c < menor:
        menor = c

print(numeros)
print(f'O maior numero foi o {maior} e o menor foi {menor}')
print(f'O maior numero foi {max(numeros)} e o menor foi {min(numeros)}')
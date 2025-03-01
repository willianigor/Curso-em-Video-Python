#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
valores = (int(input('Digite um valor\n')),int(input('Digite um valor\n')),int(input('Digite um valor\n')),int(input('Digite um valor\n')))
print(f'O numero 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posicao {valores.index(3) + 1}')
else:
    print('O valor 3 nao foi digitado')


for c in valores:
    if c % 2 == 0:
        print(c,'Eh um numero par')

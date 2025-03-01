#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
peso = [0] * 5
aux = 0

for c in range(5):
    peso[c] = float(input('Digite o peso da pessoa de numero {} em quilogramas\n'.format(c + 1)))

for a in range(5):
    aux = peso[a]
    for b in range(a + 1,5):
        if peso[a] < peso[b]:
            peso[a], peso[b] = peso[b], peso[a]

print('O maior peso equivale a: {:.2f}Kg\nO menor peso equivale a: {:.2f}Kg'.format(peso[0],peso[4]))

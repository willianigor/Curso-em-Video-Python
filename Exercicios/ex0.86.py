#Exercício Python 086:
#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0], [0,0,0], [0,0,0]]

for a in range(3):
    for b in range(3):
        matriz[a][b] = int(input(f'Digite um numero para a linha {a} e coluna {b}\n'))
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for c in range(3):
    for d in range(3):
        print(f'[{matriz[c][d]}]',end=' ')
    print('\n')
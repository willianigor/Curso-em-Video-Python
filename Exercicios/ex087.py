#Exercício Python 087: Aprimore o desafio anterior,mostrando no final:
#A)A soma de todos os valores pares digitados.
#B)A soma dos valores da terceira coluna.
#C)O maior valor da segunda linha.
matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = 0
soma_terceira = 0
maior = 0
soma_total = 0

for a in range(3):
    for b in range(3):
        matriz[a][b] = int(input(f'Digite um numero para a linha {a + 1} e coluna {b + 1}\n'))
        soma_total += matriz[a][b]
        if matriz[a][b] % 2 == 0:
            soma_par += matriz[a][b]
        if b == 2:
            soma_terceira += matriz[a][b]
        if a == 1:
            if maior <= matriz[a][b]:
                maior = matriz[a][b]
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for c in range(3):
    for d in range(3):
        print(f'[{matriz[c][d]}]',end=' ')
    print('\n')
print(f'A soma dos valores digitados foi de: {soma_total}\nA soma dos valores pares digitados foi de: {soma_par}\nA soma dos valores da terceira coluna foi de: {soma_terceira}\nO maior valor da segunda linha equivale a: {maior}')
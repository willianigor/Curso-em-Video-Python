#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
i = int(input('Digite o inicio do intervalo\n'))
f = int(input('Digite o fim do intervalo\n'))
soma = 0
cont = 0

input('Pressione ENTER e irei somar todos os numeros multiplos de 3 neste intervalo\n')

for c in range(i,f + 1):
    if c % 3 == 0:
        cont += 1
        soma += c
print('O somatorio dos numeros multiplos de 3 compreendidos no intervalo {} e {} equivale a: {}\nTOTAL DE NUMEROS IMPARES NO INTERVALO: {}'.format(i,f,soma,cont))

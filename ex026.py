#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase\n')).strip().upper()
numA = frase.count('A')

print('A letra A aparece {} vezes na frase'.format(numA))
print('A primeira letra A aparece na posicao {}\n'.format(frase.find('A') + 1))
print('A ultima letra A aparece na posicao {}\n'.format(frase.rfind('A') + 1))

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase\n')).strip().upper()
palavras = frase.split()
palavrasJuntas = ''.join(palavras)
inverso = ''
inverso1 = palavrasJuntas[::-1]

for letra in range (len(palavrasJuntas) - 1,-1,-1):
    inverso += palavrasJuntas[letra]

print(inverso1)
print(inverso)

if inverso == palavrasJuntas:
    print('Temos um palindromo!\n')
else:
    print('Nao temos um palindromo\n')

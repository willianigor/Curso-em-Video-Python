#Exercício Python 085:
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
numeros = list()
n =  0
impares = list()
pares = list()

for a in range (0,7):
    n = int(input('Digite um numero:\n'))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
impares.sort()
pares.sort()
print(f'Os numeros pares em ordem crescente sao: {pares}.\nOs numeros impares em ordem crescente sao: {impares}')
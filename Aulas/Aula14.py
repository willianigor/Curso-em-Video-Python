#Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.
r = 'S'
par = impar = 0

while r == 'S':
    numero = int(input('Digite um valor\n'))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
    r = str(input('Deseja continuar? [S/N]\n')).upper().strip()
print('Fim')
print('Voce digitou {} numeros pares e {} numeros impares'.format(par,impar))
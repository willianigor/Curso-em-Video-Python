#Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = 0
soma = 0
numero = 0
while True:
    numero = int(input('Digite um numero ou digite 999 para parar\n'))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Voce digitou {cont} numeros\nA soma entre equivale a {soma}\nFIM')

#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
n = 0
aux = 1
while True:
    n = int(input('Digite um numero e mostrarei sua tabuada ou digite um numero negativo para finalizar\n'))
    if n < 0:
        break
    while aux <= 10:
        print(f'{n} X {aux} = {n * aux}')
        aux += 1
    aux = 1
print('FIM!')
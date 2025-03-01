#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
soma = cont = n = 0


while n != 999:
    n = int(input('Digite um numero inteiro ou digite 999 para sair!\n'))
    if n != 999:
        soma += n
        cont += 1
    
print('Foram digitados {} numeros\nA soma entre eles equivale a: {}'.format(cont,soma))

#screva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
numero1 = int(input('Digite o primeiro numero inteiro\n'))
numero2 = int(input('Digite o segundo numero inteiro\n'))

if numero1 > numero2:
    print('{} eh maior que {}\n'.format(numero1,numero2))
elif numero1 < numero2:
    print('{} eh menor que {}\n'.format(numero1,numero2))
else:
    print('{} e {} sao os mesmos numeros\n'.format(numero1,numero2))
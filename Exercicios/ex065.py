#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
n = maior = soma = termos = 0
menor = 9999999999999999
opcao = ''

while True:
    n = int(input('Digite um numero\n'))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    termos += 1
    soma += n
    
    while True:
        opcao = str(input('Deseja continuar?[S/N]\n')).strip().upper()
        if opcao in ['S','N']:
            break
        opcao = str(input('OPCAO INVALIDA!\nDeseja continuar?[S/N]\n')).strip().upper()
    if opcao == 'N':
        break

print(f'Você digitou {termos} valores e a média entre eles foi {soma/termos:.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
i = int(input('Digite o intervalore desejado para saber os numeros pares contidos neste intervalo\n'))
for c in range(1,i+1):
    if c % 2 == 0:
        print('{} eh um numero par'.format(c))
for c in range(2,i,2):
    print(c)
print('Sao os numeros pares')
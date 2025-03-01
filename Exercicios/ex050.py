#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
n = [0] * 6
soma = 0
for c in range (6):
    n[c] = int(input('Digite o {}o valor\n'.format(c + 1)))
    soma += n[c]
print('A soma dos valores digitados equivale a: {}'.format(soma))

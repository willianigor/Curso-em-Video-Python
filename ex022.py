'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
 O nome com todas as letras maiúsculas e minúsculas.

 Quantas letras ao todo (sem considerar espaços).

 Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo\n')).strip
dividido = nome.split()
caracteres = len(nome)
espacos = nome.count(' ')

print('\nSeu nome em MAIUSCULAS eh: ' + nome.upper())
print('Seu nome em MINUSCULAS eh: ' + nome.lower() + '\n')
print('Seu nome completo possui {} letras\n'.format(caracteres - espacos))
print('Seu primeiro nome: {},possui {} letras\n'.format(dividido[0],len(dividido[0])))
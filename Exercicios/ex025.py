#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nomeCompleto = str(input('Digite seu nome completo\n')).strip().title()

print('Voce possui Silva no nome?\n{}\n'.format('Silva' in nomeCompleto))
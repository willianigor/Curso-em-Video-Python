#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nomeCompleto = str(input('Digite seu nome completo\n')).strip().title()
vetorNomes = nomeCompleto.split()

print('\nSeu primeiro nome: {}'.format(vetorNomes[0]))
print('Seu ultimo nome: {}\n'.format(vetorNomes[len(vetorNomes) - 1]))

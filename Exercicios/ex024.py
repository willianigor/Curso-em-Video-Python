#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite a cidade em que voce nasceu\n')).strip().capitalize()
primeiroNome = cidade.split()

print('Santo' in primeiroNome[0])
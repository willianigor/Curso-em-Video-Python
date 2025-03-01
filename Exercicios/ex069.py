#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
nome = []
idade = []
sexo = []
indice = homens = mulher_menor20 = maioresIdade  = 0
opcao = ''
while True:
    nome.append(str(input('Nome:\n')).strip().title())
    idade.append(int(input('Idade\n')))
    while idade[indice] < 0:
        idade[indice] = int(input('OPCAO INVALIDA!\nIdade\n'))
    if idade[indice] > 18:
        maioresIdade += 1
    sexo.append(str(input('Sexo [M/F]\n')).strip().upper())
    while sexo[indice] not in ['M','F']:
        sexo[indice] = str(input('OPCAO INVALIDA!\nSexo [M/F]\n')).strip().upper()
    if sexo[indice] == 'M':
        homens += 1
    if sexo[indice] == 'F' and idade[indice] < 20:
        mulher_menor20 += 1
    indice += 1
    opcao = str(input('Deseja realizar mais um cadastro? [S/N]\n')).strip().upper()
    while opcao not in ['S','N']:
        opcao = str(input('OPCAO INVALIDA!\nDeseja realizar mais um cadastro? [S/N]\n')).strip().upper()

    if opcao == 'N':
        break
print(f'Foram realizados {indice} cadastros. Dos quais:\n{maioresIdade} sao maiores de 18 anos\n{homens} sao homens\nE {mulher_menor20} sao mulheres com menos de 20 anos de idade')
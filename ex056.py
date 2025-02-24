#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nome = [''] * 4
idade = [0] * 4
sexo = [''] * 4
soma = 0
maiorIdade = 0
maisVelho = ''
cont = 0

for b in range(4):
    nome[b] = str(input('Digite o nome completo da pessoa de numero {}\n'.format(b + 1))).strip().title()
    idade[b] = int(input('Digite a idade da pessoa de numero {}\n'.format(b + 1)))
    sexo[b] = str(input('Digite o sexo(Masculino ou Feminino) da pessoa de numero {}\n'.format(b + 1))).strip().title()

for c in range(4):
    soma += idade[c]

    if sexo[c] == 'Masculino' and idade[c] > maiorIdade:
        maiorIdade = idade[c]
        maisVelho = nome[c]

    if sexo[c] == 'Feminino' and idade [c] < 20:
        cont += 1

print('A MEDIA DE IDADE DO GRUPO VALE: {:.2f}\nO homem mais velho eh o {}\nExistem {} mulheres com idade menor que 20 anos'.format(soma/4,maisVelho,cont))

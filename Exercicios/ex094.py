#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
registros = list()
mulheres = list()
acima_media = list()
soma_idade = 0

while True:
    opcao = str(input('Deseja cadastrar uma pessoa?(S/N)\n')).strip().upper()
    if opcao == 'N':
        break
    
    nome = str(input('Digite o nome:\n')).strip().title()
    sexo = str(input('Digite o sexo:(M/F)\n')).strip().upper()
    while True:
        sexo = str(input('Digite o sexo: (M/F)\n')).strip().upper()
        if sexo in ['M', 'F']:
            break
        print('Sexo inválido! Digite apenas M ou F.')
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Digite a idade:\n'))
    soma_idade += idade

    dados = {
        'nome' : nome,
        'sexo' : sexo,
        'idade' : idade,
    }

    registros.append(dados)

media = soma_idade / len(registros)

for i in registros:
    if i['idade'] > media:
        acima_media.append(i['nome'])

print(f'Foram cadastradas {len(registros)} pessoas')
print(f'A media de idade foi de {media} anos')
print('As mulheres registradas sao:')
for mulher in mulheres:
    print(f'{mulher}')
print('As pessoas com idade acima da media sao:')
for pessoas in acima_media:
    print(f'{pessoas}')

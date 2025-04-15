#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. 
#No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
maior_peso = menor_peso = 0
pessoas = list()
opcao = ''

while True:

    nome = str(input('Nome:\n'))
    peso = float(input('Peso:\n'))
    pessoas.append([nome,peso])

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso

    else:
        if maior_peso < peso:
            maior_peso = peso
        if menor_peso > peso:
            menor_peso = peso

    opcao = str(input('Deseja registrar mais alguem?\n')).strip().upper()
    if opcao == 'N':
        break

mais_leves = list()
mais_pesadas = list()

for p in pessoas:
    if p[1] == maior_peso:
        mais_pesadas.append(p[0])
for p in pessoas:
    if p[1] == menor_peso:
        mais_leves.append(p[0])

print(f'Foram registradas {len(pessoas)} pessoas\n.O maior peso registrado foi de {maior_peso} em {mais_pesadas}\n.O menor peso registrado foi de {menor_peso} em {mais_leves}')
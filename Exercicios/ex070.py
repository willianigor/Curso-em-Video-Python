#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
nomeProduto = []
preco = []
total = 0
produtosMaiores = 0
nomeBarato = opcao = ''
indice  = 0 
menorPreco = 9999999999
while True:
    nomeProduto.append(str(input('Digite o nome do produto\n')).strip().title())
    preco.append(float(input('Digite o valor do produto\nR$')))
    while preco[indice] < 0:
        preco.append(float(input('VALOR INVALIDO!\nDigite o valor do produto\nR$')))
    total += preco[indice]
    if preco[indice] > 1000:
        produtosMaiores += 1
    if preco[indice] < menorPreco:
        menorPreco = preco[indice]
        nomeBarato = nomeProduto[indice]
    indice += 1
    opcao = str(input('Deseja cadastrar mais um produto? [S/N]\n')).strip().upper()
    if opcao == 'N':
        break
print(f'O total gasto na compra foi de R${total:.2f}\n{produtosMaiores} custaram mais que R$1.000,000\n{nomeBarato} foi o produto mais barato custando R${menorPreco:.2f}')
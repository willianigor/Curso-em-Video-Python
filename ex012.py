#Crie um programa que receba do usuario o preco de um produto e mostre na tela o valor atualizado com 5% de desconto
valor = float(input('Digite o valor do produto\nR$'))
valorAtt = valor - (valor / 100) * 5

print('Parabens,voce ganhou 5% de desconto\nSeu produto saiu de R${} para R${:.2f}\n'.format(valor,valorAtt))
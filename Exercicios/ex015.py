#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias voce ficou com o carro?\n'))
rodagem = float(input('Quantos quilometros voce rodou com ele?)\n'))

valorTotal = (dias * 60) + (rodagem * 0.15)

print('O valor a ser pago pelo aluguel do carro eh de R${:.2f}\n'.format(valorTotal))
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros
valor = float(input('Digite o preco normal do produto\n'))
print('-' * 5 + 'OPCOES DE PAGAMENTO' + 5 * '-')
print('''DIGITE 1 PARA PAGAMENTO A VISTA EM DINHEIRO OU CHEQUE - 10% DE DESCONTO
DIGITE 2 PARA PAGAMENTO A VISTA NO CARTAO - 5% DE DESCONTO
DIGITE 3 PARA PAGAMENTOS EM ATE 2X NO CARTAO - SEM DESCONTO
DIGITE 4 PARA PAGAMENTOS EM 3X OU MAIS NO CARTAO - 20% DE JUROS
''')
print('-' * 5 + 'OPCOES DE PAGAMENTO' + 5 * '-')
opcao = int(input('Digite o numero da sua opcao de pagamento!\n'))

if opcao == 1:
    total = valor * 0.9
    print('Voce ganhou 10% de desconto!Seu produto devera ser pago em 1x de R${:.2f}\n'.format(total))
elif opcao == 2:
    total = valor * 0.95
    print('Voce ganhou 5% de desconto!Seu produto devera ser pago em 1x de R${:.2f}\n'.format(total))
elif opcao == 3:
    parcela = valor / 2
    print('Voce esta parcelando 2x sem juros!Cada parcela tera o valor de R${:.2f}\n'.format(parcela))
elif opcao == 4:
    total = valor * 1.2
    n = int(input('Em quantas parcelas voce deseja parcelar?\n'))
    parcela = total / n
    print('Voce ira pagar um total de R${:.2f} que serao parcelados em {}x de R${:.2f}\n'.format(total,n,parcela))
else:
    print('\033[1;31;41mOPCAO INVALIDA!!\033[m\n')


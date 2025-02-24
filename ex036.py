#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa que voce deseja comprar?\n'))
salario = float(input('Qual o seu salario?\n'))
anos = int(input('Em quantos anos voce pretende quitar essa casa?\n'))
prestacao = casa / (anos * 12)
salarioIdeal = prestacao * 10 / 3

if salario >= salarioIdeal:
    print('\033[1;32;42mSEU FINANCIAMENTO FOI APROVADO\033[m\n')
    print('O valor da prestacao sera de: R${:.2f} que serao pagos mensalmente ao longo de {} anos.'.format(prestacao,anos))

else:
    print('\033[1;33;41mSEU FINANCIAMENTO FOI REPROVADO\033[m\n')
    print('O valor da prestacao de uma casa de R${:.2f} financiada em {} anos eh de: R${:.2f} mensais\nLogo seu salario devera ser de,no minimo: R${:.2f}.\n'.format(casa,anos,prestacao,salarioIdeal))

input('Pressione ENTER para sair\n')
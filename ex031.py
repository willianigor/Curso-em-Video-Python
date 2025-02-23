#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distancia da viagem?\n'))

if distancia <= 200:
    valor = distancia * 0.5
    print('O valor a ser pago por esta viagem eh de: {}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor a ser pago por esta viagem eh de: {}'.format(valor))
print('Tenha uma otima viagem!')
input('Digite ENTER para sair\n')
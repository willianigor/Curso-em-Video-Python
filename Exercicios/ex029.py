#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidadeCarro = float(input('Qual a velocidade atual do carro?\n'))

if velocidadeCarro > 80:
    multa =  (velocidadeCarro - 80) * 7
    print('Voce esta acima do limite de velocidade!!!\nSua MULTA eh de: R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com seguranca!')

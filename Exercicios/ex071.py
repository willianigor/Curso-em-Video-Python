#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('-=' * 5 + 'BEM VINDO AO BANCO FREAK!' + 5 * '-=')
valorSaque = int(input('Qual valor voce deseja sacar?\nR$'))
total = valorSaque
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        print(f'{totalCedulas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break 
print('ATE MAIS!!\nOBRIGADO POR USAR O BANCO FREAK!')
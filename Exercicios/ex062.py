##Leia o primeiro termo e a razão de uma PA
#Mostrando os 10 primeiros termos da progressão usando a estrutura while.E melhore o programaa1 = float(input('Digite o primeiro termo da sua PA\n'))
#Perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = float(input('Digite o primeiro termo da sua PA\n'))
r = float(input('Digite a razao da sua PA\n'))
aux = 1
opcao = 1

while aux <= 10:
    print('O termo de numero {} da PA vale {}'.format(aux,a1 + (r * aux)))
    aux += 1
while opcao != 0:
    opcao = int(input('Para sair digite 0\nPara calcular a PA ate o termo de numero X digite o termo desejado.\n'))
    aux = 1
    if opcao > 0:
        while aux <= opcao:
            print('O termo de numero {} da PA vale {}'.format(aux,a1 + (r * aux)))
            aux += 1
    elif opcao < 0:
        opcao = int(input('OPCAO INVALIDA!\nPara sair digite 0\nPara calcular a PA ate o termo de numero X digite o termo desejado.\n'))

print('FIM')
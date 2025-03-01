#Leia o primeiro termo e a razão de uma PA
#Mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = float(input('Digite o primeiro termo da sua PA\n'))
r = float(input('Digite a razao da sua PA\n'))
aux = 1

while aux <= 10:
    print('O termo de numero {} da PA vale {}'.format(aux,a1 + (r * aux)))
    aux += 1
print('FIM')
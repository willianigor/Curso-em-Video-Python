#Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
#É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
#Vamos ver tambem o uso das f strings
nome = 'Jose'
salario = 3336.908
idade = 33
n = 0

print(f'{nome} tem {idade} anos e um salario no valor de R${salario:.2f}')

while True:
    n = int(input('Digite um numero ou 999 para sair!\n'))
    if n == 999:
        break
    print(f'o numero digitado foi {n}')
print('FIM!')
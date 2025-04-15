#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
opcao = ''
pares = []
impares = []
while True:
    n = float(input("Digite um valor\n"))
    lista.append(n)
    opcao = str(input("Deseja continuar?(S/N)")).upper().strip()
    if opcao == 'N':
        break
for c in range(0,len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f"Lista total: {lista}\nLista de pares: {pares}\nLista impares: {impares}")
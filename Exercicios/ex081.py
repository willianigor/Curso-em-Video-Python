#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
opcao = ''
while True:
    n = float(input("Digite um numero\n"))
    lista.append(n)
    opcao = str(input("Deseja continuar?(S/N)")).upper().strip()
    if opcao == 'N':
        break
lista.sort(reverse = True)
tamanho = len(lista)
print(f"Foram digitados {tamanho} numeros\nA lista em ordem decrescente equivale a: {lista}\n")
if 5 in lista:
    print("O numero 5 esta na lista")
else:
    print("O numero 5 nao esta na lista")
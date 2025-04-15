#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
nums = []
aux = ''
aux2 = 0
aux3 = 0
while True:
    aux2 = float(input("Digite um numero\n"))
    if aux2 in nums:
        aux2 = 0
    else:
        nums.append(aux2)
    aux = str(input("Deseja digitar mais um numero?(S/N)")).upper().strip()
    if aux == 'N':
        break
nums.sort()
print(nums)

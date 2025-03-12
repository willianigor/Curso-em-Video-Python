num = [2,5,9,1]
num[2] = 3
print(num[2])
num.append(7)
print(num[4])
#num.sort(rever=True)
num.insert(3,4)
num.insert(5,6)
num.sort()
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop(4) #Remove o valor no indice 4
print(f'Lista num apos o num.pop:  {num}')
num.remove(3) #Remove o VALOR ao inves do indice. A primeira ocorrencia do valor.
print(f'Lista num apos o num.remove():  {num}')

if 7 in num: #Checa se o valor X esta contido na lista num
    num.remove(7)
    print(f'Lista num apos o num.remove():  {num}')
else:
    print('Nao achei o numero 7')
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor\n')))
for v in valores:
    print(f'{v}...')
for a in range(len(valores)):
    print(f'Indice {a}')
    print(f'Valores: {valores[a]}')

valores1 = valores[:] #Aqui voce esta copiando os valores de valores para valores1
valores2 = valores #Aqui ha uma ligacao entre duas listas,ou seja,se modificarmos um item de qualquer uma das listas,a outra tambem sera modificada.

valores2[2] = 666

print(valores)
print(valores1)
print(valores2)
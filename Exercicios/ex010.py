#Crie um exercicio que receba do usuario um valor em reais e mostre o numero de Dolares que aquele valor consegue comprar
r = float(input('Digite um valor em reais\nR$'))
d = r / 5.73

print('R${:.2f} equivalem a ${:.2f} dolares americanos'.format(r,d))
#Crie um programa que receba do usuario um valor em metros e mostre na tela os respectivos valores em centimetros,quilomertos,decametros,decimetros,hectometros e milimetros
x = float(input('Digite um valor em metros\n'))
km = x / 10**3
hm = x / 10**2
dam = x / 10
dm = x * 10
cm = x * 10**2
mm = x * 10**3

print('O valor {} em metros corresponde a\n'.format(x))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm\n '.format(km,hm,dam,dm,cm,mm))
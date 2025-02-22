#Crie um programa que receba do usuario a altura e a largura de uma parade e mostre pra ele a area da parede e a quantidade de tinta necessaria para pinta-la. Sabe-se que 1L pinta 2m^2
a = float(input('Digite a altura da parede em metros\n'))
l = float(input('Digite a largura da parede em metros\n'))
p = a * l
q = p / 2

print('A sua parede de dimensoes {} x {} possui area de {:.2f} metros quadrados\nPortanto serao necessarios {:.2f}L de tinta para pinta-la'.format(a,l,p,q))
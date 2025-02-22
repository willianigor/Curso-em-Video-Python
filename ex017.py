#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

c1 = float(input('Digite o valor do primeiro cateto\n'))
c2 = float(input('Digite o valor do segundo cateto\n'))

h = math.sqrt(pow(c1,2) + pow(c2,2))

h2 = math.hypot(c1,c2)

print('A hipotenusa vale {:.2f}'.format(h))
print('A hipotenusa vale {:.2f}'.format(h2))
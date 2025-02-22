#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = float(input('Digite um angulo qualquer\n'))

print('O seno deste angulo vale: {:.2f}\n'.format(math.sin(math.radians(ang))))
print('O cosseno deste angulo vale: {:.2f}\n'.format(math.cos(math.radians(ang))))
print('A tangente deste angulo vale: {:.2f}\n'.format(math.tan(math.radians(ang))))
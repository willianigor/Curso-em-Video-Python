#Voce deve criar um programa que receba uma variavel do usuario e mostre na tela o dobro,o triplo e a raiz quadrada deste numero
x = float(input('Digite um numero\n'))

print('O Dobro de {} vale {} \nO triplo vale {}\nE a raiz quadrada vale {}\n'.format(x, x*2, x*3, x**(1/2)))
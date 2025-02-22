#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em grau Celsius\n'))
fahrenheit = (celsius * 9 / 5 ) + 32 

print('{:.2f}C equivalem a {:.2f}F\n'.format(celsius,fahrenheit))
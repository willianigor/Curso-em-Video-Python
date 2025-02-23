#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do seu salario\nR$'))

if salario > 1250:
    print('O valor do seu AUMENTO foi de: R${:.2f}\nLogo,seu novo salario sera de: R${}'.format(salario * 0.1,salario + salario * 0.1))
if salario <= 1250:
    print('O valor do seu AUMENTO foi de: R${:.2f}\nLogo,seu novo salario sera de: R${}'.format(salario * 0.15,salario + salario * 0.15))
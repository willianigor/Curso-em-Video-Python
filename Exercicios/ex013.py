#Crie um programa que receba do usuario o seu salario e mostre o seu novo salario com 15% de aumento
salario = float(input('Digite o seu salario atual\nR$'))
salario = salario + (salario * 15) / 100

print('Seu novo salario com aumento de 15% para o ano que vem sera de R${:.2f}\n'.format(salario))
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from datetime import date

atual = date.today().year
ano = int(input('Em que ano o atleta nasceu?\n'))
idade = atual - ano

if idade <= 9 and idade >= 0:
    print('ATLETA ENQUADRA-SE NA CATEGORIA MIRIM!')
elif idade > 9 and idade <= 14:
    print('ATLETA ENQUADRA-SE NA CATEGORIA INFANTIL!')
elif idade > 14 and idade <= 19:
    print('ATLETA ENQUADRA-SE NA CATEGORIA JUNIOR!')
elif idade > 19 and idade <= 25:
    print('ATLETA ENQUADRA-SE NA CATEGORIA SENIOR!')
elif idade > 25:
    print('ATLETA ENQUADRA-SE NA CATEGORIA MASTER!')
else:
    print('\033[1;31;41mOPCAO INVALIDA!!\033[m\n')

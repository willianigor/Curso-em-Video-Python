#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um ano\n'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} eh um ano BISSEXTO'.format(ano))
else:
    print('{} NAO eh um ano BISSEXTO'.format(ano))
input('Pressione ENTER para sair\n')
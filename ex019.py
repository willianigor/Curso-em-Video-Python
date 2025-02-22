# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

a1 = input('Digite o nome do primeiro aluno\n')
a2 = input('Digite o nome do segundo aluno\n')
a3 = input('Digite o nome do terceiro aluno\n')
a4 = input('Digite o nome do quarto aluno\n')

lista = [a1,a2,a3,a4]

escolhido = random.choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))

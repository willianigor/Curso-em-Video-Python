#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = input('Digite o nome do aluno 1\n')
a2 = input('Digite o nome do aluno 2\n')
a3 = input('Digite o nome do aluno 3\n')
a4 = input('Digite o nome do aluno 4\n')

lista = [a1,a2,a3,a4]

random.shuffle(lista)

print('A ordem de apresentacao sera:\n {}\n'.format(lista))

print('A ordem de apresentacao sera')
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3],'\n')
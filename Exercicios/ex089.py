#Exercício Python 089:
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = list()

while True:
    nome = str(input('Digite o nome do aluno:\n'))
    nota1 = float(input('Digite o a nota da P1:\n'))
    nota2 = float(input('Digite a nota da p2:\n'))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja cadastrar mais algum aluno?(S/N)')).upper().strip()
    if opcao == 'N':
        break

print('\nBoletim dos alunos:')
print(f'{"Nº":<4}{"Nome":<15}{"Média":>6}')
print('-' * 30)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<15}{aluno[2]:>6.1f}')

while True:
    opcao = int(input('\nMostrar notas de qual aluno? (Digite o número, ou 999 para sair): '))
    if opcao == 999:
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]}: {boletim[opcao][1]}')
    else:
        print('Número inválido, tente novamente.')

print('\nPrograma encerrado.')
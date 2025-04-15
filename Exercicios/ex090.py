#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
boletim = dict()

while True:
    
    opcao = str(input('Deseja cadastrar um aluno?(S/N)\n')).upper().strip()
    if opcao == 'N':
        break
    
    nome = str(input('Digite o nome do aluno:\n'))
    media = float(input('Digite a media deste aluno:\n'))

    if media >= 6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    boletim[nome] ={ 
        "media" : media,
        "situacao" : situacao
    }

for chave,dados in boletim.items():
    print(f'Nome: {chave}\n   Media: {dados['media']}\n   Situacao: {dados['situacao']}')   
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
registro = dict()

while True:

    opcao = str(input('Deseja realizar um novo cadastro?(S/N)\n')).upper().strip()
    if opcao == 'N':
        break

    nome = str(input('Digite o nome:\n')).title()
    ano_nascimento = int(input('Digite o ano de nascimento:\n'))
    idade = datetime.now().year - ano_nascimento
    ctps = int(input('Digite a CTPS:\n'))

    pessoa = {
        'nome' : nome,
        'nascimento' : ano_nascimento,
        'idade' : idade,
        'ctps' : ctps,
    }

    if ctps > 0:
        ano_contratacao = int(input('Digite o ano de contratacao\n'))
        salario = float(input('Digite o salario:\n'))
        idade_aposentadoria = idade + (ano_contratacao + 35 - datetime.now().year)
    
        pessoa['ano_contratacao'] = ano_contratacao
        pessoa['salario'] = salario
        pessoa['idade_aposentadoria'] = idade_aposentadoria
    else:
        pessoa['ano_contratacao'] = 'Nao possui'
        pessoa['salario'] = 0
        pessoa['idade_aposentadoria'] = 'Nao possui previsao'

    registro[nome] = pessoa

for chave,dados in registro.items():
    print(f"Nome: {dados['nome']}")
    print(f"  Ano de nascimento: {dados['nascimento']}")
    print(f"  Idade: {dados['idade']} anos")
    print(f"  CTPS: {dados['ctps']}")
    print(f"  Ano de contratação: {dados['ano_contratacao']}")
    print(f"  Salário: R${dados['salario']}")
    print(f"  Idade para aposentadoria: {dados['idade_aposentadoria']}")
    print("-" * 40)

#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
anos = [0] * 7
anoAtual = datetime.date.today().year
aux = 0
aux1 = 0

for c in range(7):
    anos[c] = int(input('Digite o ano de nascimento da pessoa de numero {}\n'.format(c + 1)))

for a in range(7):
    if anoAtual - anos[a] >= 18:
        print('A pessoa de numero {} ja atingiu a maioridade'.format(a + 1))
        aux += 1
    elif anoAtual - anos[a] < 18 and anoAtual - anos[a] >= 0:
        aux1 += 1
    else:
        print('OPCAO INVALIDA PARA A PESSOA DE NUMERO {}'.format(a + 1))

print('Portanto\n{} pessoas ja atingiram a maioridade\n{} pessoas nao atingiram a maioridade\n'.format(aux,aux1))
#Nessa aula, vamos aprender como utilizar estruturas condcionais simples e compostas nos seus programas em Python.
tempo = 2025 - int(input('Digite o ano do seu carro\n'))

if tempo <= 5:
    print('Seu carro eh um carro novo\n')
else:
    print('Seu carro ja eh um carro antigo\n')
print('-----FIM-----')
#Condicao simplificada
print('Carro novo' if tempo <= 5 else 'Carro antigo')
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo [M/F]\n')).strip().upper()

while sexo not in ['M', 'F']:
    sexo = str(input('Opcao invalida.Digite seu sexo [M/F]\n')).strip().upper()
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso!')
else:
    print('Sexo Feminino registrado com sucesso!')
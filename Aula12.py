#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
nome = str(input('Digite seu nome\n')).strip()

if nome == 'Igor':
    print('Ola,Freak\n')
elif nome == 'Freak':
    print('Ola,Igor\n')
elif nome == 'Maria' or 'Joao' or 'Matheus':
    print('Seu nome eh bem popular no Brasil\n')
else:
    print('Ola, {}'.format(nome))
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite o numero que deseja converter\n'))
print('-' * 5 + 'DIGITE 1 PARA BINARIO' + 5 * '-')
print('-' * 5 + 'DIGITE 3 PARA OCTAL' + 5 * '-')
print('-' * 5 + 'DIGITE 3 PARA HEXADECIMAL' + 5 * '-')
escolha = int(input('Digite a opcao que deseja converter o seu numero\n'))
if escolha == 1:
    print('{} EM BINARIO EH IGUAL A: {}\n'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('{} EM OCTAL EH IGUAL A: {}\n'.format(numero,oct(numero)[2:]))
elif escolha == 3:
    print('{} EM HEXADECIMAL EH IGUAL A: {}'.format(numero,hex(numero)[2:]))
else:
    print('\033[1;31;41mOPCAO INVALIDA!!!\033[m\n')

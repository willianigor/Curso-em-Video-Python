#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota\n'))
n2 = float(input('Digite a segunda nota\n'))
media = (n1 + n2) / 2

print('A media deste aluno vale: {:.2f}\n'.format(media))

if media < 5:
    print('\033[1;31;41mREPROVADO!!!\033[m\n')
elif media >= 5 and media <= 6.999999999999999:
    print('\033[1;33;43mRECUPERACAO!\033[m\n')
else:
    print('\033[1;32;42mAPROVADO!!!\033[m\n')


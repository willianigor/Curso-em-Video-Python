# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Em que ano voce nasceu?\n'))
atual = date.today().year
idade = atual - ano

print('Quem nasceu em {} tem {} anos em {}\n'.format(ano,idade,atual))

if idade == 18:
    print('\033[1;32;42mVOCE DEVE FAZER O ALISTAMENTE NESTE ANO!!!\033[m\nDIRIJA-SE A JUNTA MILITAR DO SEU MUNICIPIO MAIS PROXIMA!!')
elif idade < 18:
    falta = 18 - atual + ano
    print('\033[1;33;43mSEM PROBLEMAS,FALTAM {} ANOS PARA O SEU ALISTAMENTO!\033[m\n'.format(falta))
    
else:
    passou =(ano - atual) + 18
    print('\033[1;31;41mVOCE ESTA ATRASADO COM SUA OBRIGACAO MILITAR!!!\033[m\nPassaram-se {} anos do seu prazo de alistamento\n'.format(passou * -1))

input('Aperte ENTER para sair')
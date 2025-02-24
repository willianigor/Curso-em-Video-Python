#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:
#for c in range(0, 4):
##print(‘Acabou’)
for c in range(0,6):
    print('Ola mundo',c)
for a in range(0,7,2):
    print('Teste',a)

n = int(input('Digite um numero\n'))

for c in range(0,n + 1):
    print('Aqui esta',c,'de um total de',n)
    
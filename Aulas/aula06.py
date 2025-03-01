#Eh necessario especificar o tipo primitivo da variavel antes da funcao input
n1 = float(input('Digite um valor\n'))
n2 = float(input('Digite outro valor\n'))
s = n1 + n2
n = input('Digite algo')


#Uma forma mais eficiente de se usar a funcao print eh usando a funcao format para chamar as variaveis a serem mostradas no output
#Em que se usa as chaves dentro das aspas para mostrar onde a variavel deve ser inserida
print(type(n1),'\n','A soma entre {} e {} vale {}\n'.format(n1,n2,s))
print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#Ha diversas funcoes que checam as variaveis,eh possivel ve-las ao digitar is.
print(n.isalpha())

#Para fazer com que o programa mantenha-se aberto durante a execucao e o usuario escolha quando fecha-lo pode-se usar um comando input em que o usuario digita enter para sair do programa.
input('Pressione Enter para sair')
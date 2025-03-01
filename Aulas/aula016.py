lanche = ('Hamburguer','Suco','Pizza','Pudim')
#Tuplas sao IMUTAVEIS!Ou seja,nao se pode alterar o conteudo durante o programa.
#lanche[1] = 'Refrigerante'
#print(lanche[1])
print(lanche)
#print(lanche[1:])
#print(lanche[:3])
#print(lanche[0])
#print(lanche[1:3])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for c in range(0,len(lanche)):
    print(f'Vou comer {lanche[c]}')

for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba')
#A funcao sorted() mostra os elementos da tupla de forma ordenada.
print(sorted(lanche))
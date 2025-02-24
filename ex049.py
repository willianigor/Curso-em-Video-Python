#Faca a tabuada do numero que o usuario digitar utilizando o laco for
n = int(input('Digite um numero e te direi a sua tabuada\n'))

input('Aperte ENTER para saber a tabuada do {}'.format(n))

for c in range(1,11):
    print('{} X {:2} = {:2}'.format(n,c,n*c))
    
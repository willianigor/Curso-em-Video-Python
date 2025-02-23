#Pode-se importar apenas as funcoes que serao utilizadas no programa tambem,porem quando fizer isto ao chamar a funcao nao ha a necessidade utilizar o 'math.funcao',utiliza-se apenas a funcao()
#from math import sqrt,ceil
import math

num = float(input('Digite um numero\n'))

print('O valor da raiz quadrada de {} vale {:.2f}\n'.format(num,math.ceil(math.sqrt(num))))
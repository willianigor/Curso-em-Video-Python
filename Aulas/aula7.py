#Abaixo sera mostrado os operadores aritmeticos em Python
x = float(input('Digite um numero\n'))
y = float(input('Digite mais um numero\n'))
s = x + y
m = x * y
ss = x - y
d = x / y
di = x // y
p = x ** y
r = x % y


print('A soma vale {}\n'.format(s))
print('A multiplicacao vale {}\n'.format(m))
print('A subtracao vale {}\n'.format(ss))
print('A divisao vale {:.3f}\n'.format(d))
print('A divisao inteira vale {}\n'.format(di))
print('A potenciacao vale {}\n'.format(p))
print('O resto da divisao vale {}\n'.format(r))

input('Pressione Enter para sair')
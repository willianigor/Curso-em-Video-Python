'''Nessa aula, vamos aprender operações com String no Python.
 As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), 
 transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().'''
frase = 'Curso em video Python'
dividido = frase.split()

print(dividido[0])
print(frase[0:14])
print(frase.count('o'))
print(len(frase))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Python'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())

print(''' Claro! Aqui está uma receita simples de bolo de chocolate:

Bolo de Chocolate Simples

Ingredientes:

2 xícaras de farinha de trigo
1 xícara de açúcar
1/2 xícara de achocolatado em pó
3/4 de xícara de óleo
1 xícara de leite
3 ovos
1 colher de fermento em pó
1 pitada de sal
Modo de Preparo:

Preaqueça o forno a 180°C.
Bata os ovos, o açúcar e o óleo no liquidificador até formar uma mistura homogênea.
Adicione a farinha, o achocolatado, o leite e o sal e bata novamente até ficar bem misturado.
Misture o fermento à massa e mexa delicadamente.
Unte uma forma com óleo e farinha, despeje a massa e leve ao forno por cerca de 35-40 minutos, ou até que o palito saia limpo.
Deixe esfriar e sirva! 😋''')
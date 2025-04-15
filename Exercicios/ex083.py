#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input("Digite a expressao matematica\n"))
lista = []
cont1 = 0
cont2 = 0
for simb in expressao:
    if simb == '(':
        cont1 +=1
    elif simb == ')':
        cont2 += 1
if cont1 == cont2:
    print("Sua expressao esta CORRETA!!")
else:
    print("Sua expressao esta ERRADA!!")
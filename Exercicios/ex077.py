#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for c in range(0,len(palavras)):
    print(f'Na palavra {palavras[c].upper()} temos as vogais:', end = '')
    for letra in palavras[c]:
        if letra.upper() in 'AEIOU':
            print(letra, end = ' ')
    print('\n')
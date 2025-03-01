#Cria um programa que leia um input e diga seu tipo primitivo e todas suas caracteristicas com o comando is...\
x = input('Digite algo\n')

print('{} eh do tipo'.format(x),type(x))
print('Eh numerico?',x.isalnum(),
      '\nEh alfabetico?',x.isalpha(),
      '\nEh um numero decimal?',x.isdecimal(),
      '\nEh um numero?',x.isnumeric(),
      '\nEh alfanumerico?',x.isalnum(),
      '\nEh composto apenas de letras maiusculas?',x.isupper(),
     '\nEh o caractere espaco?',x.isspace(),
     '\nEsta capitalizada?',x.istitle(),
    '\nEh composto apenas de letras minusculas?',x.islower(),
     '\nPode ser escrito na tela?',x.isprintable())


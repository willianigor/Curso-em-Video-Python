##Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Acrescente o recurso de mostrar que tipo de triângulo será formado:ESCALENO,ISOSCELES OU EQUILATERO
r1 = float(input('Digite a reta 1\n'))
r2 = float(input('Digite a reta 2\n'))
r3 = float(input('Digite a reta 3\n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32;42mAS RETAS PODEM FORMAR UM TRIANGULO!!\033[m\n')
        
    if r1 == r2 and r2 == r3:
        print('\033[1;33;43mO TRIANGULO FORMADO SERA UM TRIANGULO EQUILATERO!\033[m\n')
    elif r1 != r2 and r2 != r3:
        print('\033[1;33;43mO TRIANGULO FORMADO SERA UM TRIANGULO ESCALENO!\033[m\n')
    else:
        print('\033[1;33;43mO TRIANGULO FORMADO SERA UM TRIANGULO ISOSCELES!\033[m\n')

else:
    print('\033[1;31;41mAS RETAS NAO PODEM FORMAR UM TRINAGULO!\033[m\n')

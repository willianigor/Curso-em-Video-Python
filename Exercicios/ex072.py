 #Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeroExtenso = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:

    index = int(input('Digite um numero de 0 a 20 e irei exibi-lo por extenso\n'))

    if 0 <= index <= 20:
        print(numeroExtenso[index])
        break\
        
    else:
        index = int(input('OPCAO INVALIDA!Digite um numero de 0 a 20 e irei exibi-lo por extenso\n'))

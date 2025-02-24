#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu peso em kg\n'))
altura = float(input('Digite sua altura em metros\n'))
imc = peso / (altura * altura)

if imc > 0 and imc < 18.5:
    print('\033[1;33;43mVOCE TEM {} DE IMC E ESTA ABAIXO DO PESO!\033[m\n'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('\033[1;32;42mVOCE TEM {} DE IMC E ESTA NO PESO IDEAL!\033[m\n'.format(imc))
elif imc >= 25 and imc < 30:
    print('\033[1;33;43mVOCE TEM {} DE IMC E ESTA EM SOBREPESO!\033[m\n'.format(imc))
elif imc >= 30 and imc <= 40:
    print('\033[1;31;41mATENCAO!!SEU IMC VALE {} E VOCE ESTA COM UM QUADRO DE OBESIDADE!\033[m\n'.format(imc))
elif imc > 40:
        print('\033[1;31;41mATENCAO!!SEU IMC VALE {} E VOCE ESTA COM UM QUADRO DE OBESIDADE MORBIDA!!!!\033[m\n'.format(imc))
else:
     print('\033[1;31;41mOPCAO INVALIDA!\033[m\n')







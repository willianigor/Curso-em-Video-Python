#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lapis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2222,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.9,'-')
index = 0

print('-' * 5)
print('LISTAGEM DE PRECOS')
print('-' * 5)

while produtos[index] != '-':
    print(f'{produtos[index]}','-' * 5,f'R${produtos[index + 1]:.2f}')
    index += 2
print('-' * 5)

# Crie um programa que tenha uma tupla única com nomes de 
# produtos e seus respectivos preços, na sequência. No final, 
# mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('lapis',1.75,
            'borracha', 2,
            'caderno',15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'canetas',22.30,
            'livro',34.90)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')

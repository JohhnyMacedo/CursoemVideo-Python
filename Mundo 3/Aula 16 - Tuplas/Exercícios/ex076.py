# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Lápis', 1.75,
'Borracha', 2.00,
'Caderno', 15.90,
'Estojo', 25.00,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 120.32,
'Caneta BIC', 2.30,
'Livro de Português', 34.90)
print('-' * 45)
print(f'{"Livraria - Preços":^45}')
print('-' * 45)
for pos, n in enumerate(lista):
    if pos % 2 == 0:
        print(f'{n:.<35}', end = '')
    else:
        print(f'R${n:7.2f}')
print('-' * 45)
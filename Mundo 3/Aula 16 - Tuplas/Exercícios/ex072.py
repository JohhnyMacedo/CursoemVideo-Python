# Crie um programa que tenha uma tupla totalmente preenchida por uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número do teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = (int(input('Digite um número de 0 a 20. ')))
while num not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
    num = (int(input('Inválido. Digite um número de 0 a 20. ')))
print(f'O número {num} se escreve {extenso[num]} por extenso.')

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes aparece o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = (int(input('Digite um valor numérico: ')), 
int(input('Digite outro valor: ')), 
int(input('Digite o 3o valor: ')), 
int(input('Digite o último valor: ')))
print(f'O número 9 apareceu {tupla.count(9)} vez(es).')
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3+1)}.')
else:
    print(f'O número 3 não apareceu entre os valores digitados.')
print(f'Os números pares que você digitou foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')

tupla = ('Aprender',
'Programar',
'Linguagem',
'Python',
'Curso',
'Gratis',
'Estudar',
'Praticar',
'Trabalhar',
'Mercado',
'Programador',
'Futuro')
for palavra in tupla:
    print(f'\n Na palavra {palavra.upper()} temos', end = ' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end = '')
# A grande sacada desse exercício é a percepção de que cada letra dentro de uma string pode ser visto como um elemento dentro de uma tupla. Ou seja, é possível analisar letra por letra ao criar um loop 'for' dentro de outro loop 'for'. O 1o loop têm como parâmetro cada elemento da tupla. Enquanto o 2o tem como parâmetro cada elemento da string, ou seja, cada letra.
# Manipulação de Strings
---
As anotações aqui presentes vão se resumir a uma listagem de comandos para a manipulação de strings. São eles:
## Fatiamento
* Pra fatiar uma String (ou mesmo retirar um elemento de uma lista, tupla ou dicionário) é só escrever o nome da variável (aqui vamos usar 'exemplo') e logo após a posição do elemento a ser fatiado entre colchetes. `exemplo[9]`. 
* Caso deseje fatiar um período (ou múltiplos elementos) basta explicitar o período com a utilização de :. `exemplo[9:15]`. 
* Você pode também adicionar um 'pace' ao fatiamento, utilizando um segundo:. `exemplo[9:15:2]`.
## Análise
* O comando `len()` retorna a quantidade de caracteres presentes em uma string (ou a quantidade de elementos presentes em uma lista).
* O comando `exemplo.count('')` retorna a quantidade de vezes que algum caractere específico (explicitado dentro das aspas dentro dos parênteses) aparece na string (ou dentro de uma lista).
   * Também é possível usar o `exemplo.count('')` em um fatiamento, sendo executado dessa forma: `exemplo.count('exemplo', 0, 20)`. É interessante perceber que aqui o início e o final do fatiamento são separados por vírgula, e não dois pontos.
* O comando `exemplo.find('exemplo')` retorna a posição de algum elemento, explicitado dentro das aspas dentro dos parênteses, dentro de uma string (ou lista).
## Transformação
* O comando `exemplo.replace('exemplo1', 'exemplo2')` localiza e troca um elemento dentro de uma string por outro (não tenho certeza, mas imagino que também deva funcionar para listas).
* `exemplo.upper()` transforma todos os caracteres em maiúsculos.
* `exemplo.lower()` transforma todos os caracteres em minúsculos.
* `exemplo.capitalize()` transforma o primeiro caractere de uma string em maiúsculo e transforma todo o restante em minúsculo.
* `exemplo.title()` transforma todos os 1os caracteres de cada palavra em maiúsculos.
* `exemplo.strip()` remove todos os espaçamentos "inúteis" no início e no final de uma string. OBS: Não remove os espaçamentos entre palavras, apenas os que estão no início e no final da string.
* `exemplo.rstrip()` basicamente faz a mesma função de .strip(), porém removendo somente os espaçamentos à direita. De forma similar, existe o `exemplo.lstrip()`.
## Divisão
* `exemplo.split()` gera uma lista com todas as palavras de uma cadeia de caracteres, utilizando os espaçamentos como parâmetro. Vale mensionar que agrega também algumas funcionalidades extras, que você pode acessar digitando comandos dentro dos parênteses. 
## Junção
* `'-'.join(exemplo)` junta elementos presentes em uma variável (exemplo) utilizando um caractere explicitado antes do ponto entre aspas ('-').
## Alinhamentos
* Os alinhamentos são utilizados na formatação de um print, sendo dessa forma:
   * Sempre presentes dentro de {}.
   * `{:40}`, alinha os elementos presentes no chaveamento dentro de 40 espaçamentos.
   * `{:^40}`, alinha os elementos presentes no chaveamento dentro de 40 espaçamentos de forma centralizada.
   * `{:>40}`, alinha à direita.
   * `{:<40}`, alinha à esquerda.
   * `{:.^40}`, alinhará a string centralizada dentro de 40 caracteres, entre ".".
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre: A) Apenas os 5 primeiros colocados; B) Os últimos 4 colocados; C) Uma lista com os times em ordem alfabética; D) Em que posição está o time da Chapecoense.

brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
menu = 0
while menu not in ('A', 'B', 'C', 'D'):
    menu = input(' A) Quais foram os 5 primeiros colocados do Brasileirão 2021?\n B) Quais foram os 4 últimos colocados do Brasileirão 2021?\n C) Liste os times que participaram do Brasileirão 2021 em ordem alfabética;\n D)Em que posição a Chapecoense ficou no Brasileirão 2021?\n\n Digite a letra (A, B, C ou D) correspondente à opção desejada: ').upper()
if menu == 'A':
    print(f'Os 5 primeiros colocados do Brasileirão 2021, do 1o ao 5o, foram: {brasileirao[0:5]}')
elif menu == 'B':
    print(f'Os 4 últimos colocados do Brasileirão 2021, do 16o ao 20o, foram {brasileirao[-4:]}')
elif menu == 'C':
    print(f'Segue abaixo a lista dos times que compuseram o Brasileirão 2021 em ordem alfabética:\n {sorted(brasileirao)}')
elif menu == 'D':
    print(f'O time da Chape ficou em {brasileirao.index("Chapecoense")+1}')

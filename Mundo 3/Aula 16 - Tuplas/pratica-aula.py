lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') 
# Lanche é uma tupla. Uma variável composta e imutável definida por ()
print(lanche[1:3]) 
# As ferramentas de fatiamento de strings também funcionam para tuplas.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
# A variável 'pos' é atribuída à enumerate e a variável comida é atribuída à 'lanche' devido a ordem de escrita.

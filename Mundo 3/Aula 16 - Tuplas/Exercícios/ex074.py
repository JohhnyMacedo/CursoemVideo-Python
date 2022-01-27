# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
nums = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20)) 
print(f'Sorteei os valores {nums[0]}, {nums[1]}, {nums[2]}, {nums[3]} e {nums[4]}')
print(f'O maior valor sorteado foi {max(nums)}.')
print(f'O menor valor sorteado foi {min(nums)}.')
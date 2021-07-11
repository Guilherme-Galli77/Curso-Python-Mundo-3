#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
Tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os valores sorteados foram {Tupla}")

for n in Tupla:
    if n == Tupla[0]:
        menor = n
        maior = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"O maior valor sorteado foi {maior}") #Posso usar ao inves de {maior} {max(Tupla)}
print(f"O menor valor sorteado foi {menor}") #Posso usar ao inves de {menor} {min(Tupla)}
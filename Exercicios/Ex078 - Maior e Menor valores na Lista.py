#Exercício Python 078: Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
print(f"Você digitou os valores: {valores}")

for c, valor in enumerate(valores):
    if c == 0:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"O maior valor digitado foi {maior} nas posiçoes ", end="")
for c, valor in enumerate(valores):
    if valor == maior:
        print(f"{c}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posiçoes ", end="")
for c, valor in enumerate(valores):
    if valor == menor:
        print(f"{c}...", end="")
print()

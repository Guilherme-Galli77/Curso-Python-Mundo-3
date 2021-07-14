# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list()
c = 0
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c += 1
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    while r not in "NnSs":
        print("Entrada inválida, digite novamente! ")
        r = str(input("Quer continuar? [S/N] ")).strip().upper()
    if r == "N":
        break
print("="*50)
print(f"Ao todo você cadastrou {c} pessoas! ") #Pode usar len(pessoas)
print(f"O maior peso foi de {maiorPeso} Kg. Peso de ", end="")

for p in pessoas:
    if p[1] == maiorPeso:
        print(f"{p[0]}", end=" ")
print()
print(f"O maior peso foi de {menorPeso} Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menorPeso:
        print(f"{p[0]}", end=" ")
print()

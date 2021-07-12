#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
impar = list()

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if r == "N":
        break
print("="*40)
print(f"A lista completa é: {lista}")
print(f"A lista de pares é: {par}")
print(f"A lista de impares é: {impar}")

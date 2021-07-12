# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
c = 0
lista = list()

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    c += 1
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if r == "N":
        break
print(f"Você digitou {c} elementos") #posso usar len(lista) ao invés de um contador
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")

if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")

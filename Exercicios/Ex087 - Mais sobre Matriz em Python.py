# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaTerceira = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição[{l},{c}]: "))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            somaTerceira += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print("="*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end="")
    print()
print("="*40)
print(f"A soma dos valores pares é {somaPares}")
print(f"A soma dos valores da terceira coluna é {somaTerceira}")
print(f"O maior valor da segunda linha é {maior}")


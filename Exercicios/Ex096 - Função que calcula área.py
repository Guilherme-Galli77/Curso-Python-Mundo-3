# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print("="*40)
    print(f"A área de um terreno {l:.2f} X {c:.2f} é de {area} m2")


larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)
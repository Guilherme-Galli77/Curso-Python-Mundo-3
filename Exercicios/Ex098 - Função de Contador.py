# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contagem(a, b, p):
    print("=" * 40)
    for c in range(a, b, p):
        print(f" {c}",end="")
    print(" FIM!")


contagem(1, 11, 1)
contagem(10, -1, -2)
print("=" * 40)
print("PERSONALIZE SUA CONTAGEM: ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print(f"Contagem de {inicio} até {fim} contando de {passo} em {passo}")
if fim > 0:
    contagem(inicio, fim+1, passo)
else:
    contagem(inicio, fim-1, passo)

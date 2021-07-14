# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.
dados = list()

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1+n2)/2
    dados.append([nome, [n1, n2], media])
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    while r not in "NnSs":
        print("Entrada inválida, digite novamente! ")
        r = str(input("Quer continuar? [S/N] ")).strip().upper()
    if r == "N":
        break
print(f"{'No.':<4} {'NOME':<10} {'MEDIA':>8}")
print("="*40)
for i, a in enumerate(dados):
    print(f"{i:<4} {a[0]:<10}{a[2]:>8.1f}")
print("="*40)

while True:
    opc = int(input("Mostrar notas de qual aluno ? (999 interrompe) "))
    if opc == 999:
        break
    if opc <= len(dados) -1:
        print(f"Notas do aluno {dados[opc][0]} : {dados[opc][1]}")

print("FIM")


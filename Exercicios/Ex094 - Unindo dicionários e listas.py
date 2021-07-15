# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = dict()
todos = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
    while pessoa["Sexo"] not in "MFmf":
        print("Entrada inválida, digite novamente! ")
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    todos.append(pessoa.copy())
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    while r not in "NnSs":
        print("Entrada inválida, digite novamente! ")
        r = str(input("Quer continuar? [S/N] ")).strip().upper()
    if r == "N":
        break

print(todos)
print(f"Ao todo temos {len(todos)} pessoas cadastradas")
media = soma / len(todos)
print(f"A média de idade é {media:5.2f} anos.")
print("As mulheres cadastradas foram: ", end="")
for p in todos:
    if p["Sexo"] in "Ff":
        print(f"{p['Nome']}", end=",")
print()
print("Lista das pessoas que estão acima da média: ", end="")
for p in todos:
    if p["Idade"] >= media:
        print('    ')
        for k,v in p.items():
            print(f"{k} = {v}; ", end="")
        print()

print('='*40)
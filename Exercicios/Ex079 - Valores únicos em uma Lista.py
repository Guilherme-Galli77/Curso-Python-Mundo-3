#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

Lista = list()

while True:
    valor = int(input("Digite um valor: "))
    if valor not in Lista:
        Lista.append(valor)
        print("Valor adicionado! ")
    else:
        print("Valor duplicado! Não vou adicionar na lista! ")
    continuar = str(input("Quer continuar [S/N] ? ")).strip().upper()
    if continuar == "N":
        break

Lista.sort()
print(f"Você digitou os valores {Lista}")
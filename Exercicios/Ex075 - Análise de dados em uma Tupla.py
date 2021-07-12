#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

Tupla = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
         int(input("Digite mais um número: ")), int(input("Digite o ultimo número: ")))

print(f"Você digitou os valores: {Tupla}")
print(f"O número 9 apareceu {Tupla.count(9)} vezes")
if 3 in Tupla:
    print(f"O valor 3 apareceu na {Tupla.index(3)+1} posicao")
else:
    print("O valor 3 não aparece na tupla")
print("Os valores pares digitados foram: ", end="")
for n in Tupla:
    if n % 2 == 0:
        print(n, end=" ")



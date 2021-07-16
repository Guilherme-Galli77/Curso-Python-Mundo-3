# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    cont = m = 0
    print("="*50)
    print("Analisando os valores...")
    for n in num:
        print(f"{n}", end=" ")
        if cont == 0:
            m = n
        if n > m:
            m = n
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior número analisado foi: {m}")


maior(2, 9, 4, 5, 1, 7)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
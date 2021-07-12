#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.
print("="*40)
print("             CARDÀPIO              ")
listagem = ("Hamburguer", 15.75,
            "Batata", 9.50,
            "Nuggets", 10.50,
            "Milkshake", 12.30,
            "X Burguer", 16.75,
            "X Salada", 19.80,
            "X Tudo", 23.50,
            "Hotdog", 14.00,
            "Refri", 6.00)
print("="*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f"{listagem[item]:.<30}", end="")
    else:
        print(f"R$ {listagem[item]:>7.2f}")
print("="*40)

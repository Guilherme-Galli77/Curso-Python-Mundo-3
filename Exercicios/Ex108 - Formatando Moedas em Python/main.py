# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

import moeda

preco = float(input("Digite o preço: R$ "))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))

moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentando(preco, aumento)
moeda.diminuindo(preco, desc)
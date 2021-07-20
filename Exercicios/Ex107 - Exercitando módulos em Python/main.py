# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input("Digite o preço: R$ "))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))

moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentando(preco, aumento)
moeda.diminuindo(preco, desc)
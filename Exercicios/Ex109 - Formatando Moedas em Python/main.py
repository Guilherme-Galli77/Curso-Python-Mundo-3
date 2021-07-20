# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.

import moeda

preco = float(input("Digite o preço: R$ "))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))


moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentando(preco, aumento)
moeda.diminuindo(preco, desc)
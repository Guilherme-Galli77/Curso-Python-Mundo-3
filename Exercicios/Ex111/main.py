# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from Ex111.utilidades import *

preco = float(input("Digite o preço: R$ "))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))


moeda.dobro(preco)
moeda.metade(preco)
moeda.aumentando(preco, aumento)
moeda.diminuindo(preco, desc)
moeda.resumo(preco, aumento, desc)
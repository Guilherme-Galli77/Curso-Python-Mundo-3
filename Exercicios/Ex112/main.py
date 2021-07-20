# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie
# uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de
# dados para aceitar apenas valores que seja monetários.

from Ex112.utilidades import *

preco = int(input("Digite o preço: R$ ").replace(",", "."))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))

dado.leiaDinheiro(preco)
moeda.resumo(preco, aumento, desc)
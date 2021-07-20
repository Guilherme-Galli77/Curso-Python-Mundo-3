# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

preco = float(input("Digite o preço: R$ "))
aumento = float(input("Digite o aumento em % : "))
desc = float(input("Digite o desconto em % : "))

moeda.resumo(preco, aumento, desc)
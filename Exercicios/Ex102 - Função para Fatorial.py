# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    --> Faz o calculo do fatorial de um numero
    :param num: Numero a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f"{c} X ",end="")
            else:
                print(f"{c} = ",end="")
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)

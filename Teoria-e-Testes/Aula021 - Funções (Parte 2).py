# Digitar no python console
# help()
help(print())  # Outro jeito (pela linha de código)

print(input.__doc__)  # Mostra a documentação do comando


# DocStrings

def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM")


help(contador)


# Parametros opcionais:

def somar(a=0, b=0, c=0):
    """
    --> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f"A soma vale {s}")


somar(2, 3, 5)  # Funciona normal
somar(3, 2)  # ERRO,se mudar o c para c=0 a função executa normalmente
somar(3)  # ERRO, se mudar o  b e c para b=0 e c=0 a função executa normalmente
somar()  # Funciona se colocar todos os parametros =0 na declaração da função
# somar(3, 3, 5, 8) #ERRO, tem que colocar o * pra funcinar
# help(print) # Para ver os parametros opcionais
somar(b=4, c=2)  # Outra forma de print sem a letra a


# Escopo de váriaveis

def teste():
    x = 8  # Variavel local
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")


# Programa principal
n = 2  # Variavel global
print(f"No programa principal, n vale {n}")
print(f"No programa principal, x vale {x}")  # ERRO, pois só funciona na função

teste()


def funcao():
    n1 = 4
    print(f"n1 detro vale {n1}")  # Print 4


n1 = 2
funcao()
print(f"n1 fora vale {n1}")  # Print 2

# Para usar variavel global dentro da função:
# usar global nome dentro da função


# Retorno de valores

def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somar2(3, 2, 5)
resp2 = somar2(1, 7)
resp3 = somar2(4)
print(f"Respostas`{resp},{resp2},{resp3}")

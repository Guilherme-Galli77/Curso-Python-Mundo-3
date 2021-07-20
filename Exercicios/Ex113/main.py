# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Problema com os dados digitados! Digite um numero valido! ")
            continue
        except KeyboardInterrupt:
            print("O usuario optou por nao informar o valor")
            return 0
        else:
            return numero


numero = leiaInt("Digite um valor: ")
print(f"O valor digitado foi {numero}")
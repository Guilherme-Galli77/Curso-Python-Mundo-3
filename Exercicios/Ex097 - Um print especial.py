# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def printEspecial(msg):
    tam = len(msg)
    print("~"*tam)
    print(msg)
    print("~"*tam)


printEspecial("Guilherme")
printEspecial("Curso de Python")
printEspecial("Teste")
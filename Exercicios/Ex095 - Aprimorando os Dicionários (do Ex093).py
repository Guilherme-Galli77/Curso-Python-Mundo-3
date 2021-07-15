# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
lista = list()
todos = list()
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    lista.clear()
    for x in range(0, tot):
        lista.append(int(input(f"Quantos gols na partida {x+1}? ")))
    jogador["Gols"] = lista[:]
    jogador["Total"] = sum(lista)
    todos.append(jogador.copy())
    r = str(input("Quer continuar? [S/N] ")).strip().upper()
    while r not in "NnSs":
        print("Entrada inválida, digite novamente! ")
        r = str(input("Quer continuar? [S/N] ")).strip().upper()
    if r == "N":
        break

print("="*40)
print("Cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}",end="")
print()
print("="*40)
for k, v in enumerate(todos):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("="*40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (digite 999 para parar)"))
    if busca == 999:
        break
    if busca >= len(todos):
        print("ERRO!! Não foi encontrado um jogador com esse código! ")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {todos[busca]['Nome']}: ")
        for i, g in enumerate(todos[busca]['Gols']):
            print(f"No jogo {i+1} fez {g} gols. ")
    print("="*40)
print("VOLTE SEMPRE")
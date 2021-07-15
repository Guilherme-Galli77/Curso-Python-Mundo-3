# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
lista = list()
totgols = cont = 0
dados["Nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))
for x in range(0, partidas):
    gols = int(input(f"Quantos gols na partida {x+1}? "))
    totgols += gols
    lista.append(gols)
dados["Gols"] = lista
dados["Total"] = totgols
print("="*40)
print(dados)
print("="*40)

for k, v in dados.items():
    print(f" O campo {k} tem o valor {v}")
print("="*40)

print(f"O jogador {dados['Nome']} jogou {partidas} partidas: ")
for g in dados['Gols']:
    print(f"--> Na partida {cont+1}, fez {g} gols.")
    cont += 1
print(f"Foi um total de {totgols} gols! ")
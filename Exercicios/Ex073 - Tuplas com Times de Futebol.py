#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Ingles de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 3 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Leicester.

Times = ("Man. City", "Man. United", "Liverpool", "Chelsea", "Leicester",
         "West Ham", "Tottenham", "Arsenal", "Leeds",
         "Everton", "Aston Villa", "Newcastle", "Wolves",
         "C.Palace", "Southampton", "Brighton", "Burnley",
         "Fulham", "West Brom", "Sheffield United")

print(f"Classificação Premier League: {Times}")
print(f"Os 5 primeiros times são: {Times[0:5]}")
print(f"Os ultimos 3 colocados e rebaixados para a Championship foram: {Times[-3:]}")
print(f"Em ordem alfabetica: {sorted(Times)}")
print(f"O Leicester está em {Times.index('Leicester')+1} lugar")


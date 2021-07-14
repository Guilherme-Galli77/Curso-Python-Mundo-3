pessoas = {"Nome": "Guilherme", "Sexo": "M", "Idade": 20}
print(pessoas["Nome"]) #Print do conteudo de nome
print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos") #Print composto
print(pessoas.keys()) #Printa as chaves(index)
print(pessoas.values()) #Printa os valores/conteudos
print(pessoas.items()) #Printa os index e conteudos
print("="*40)
#Print com for
for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

# Print composto
for k, v in pessoas.items():
    print(f"{k} = {v}")

del pessoas["Sexo"] #Deleta um elemento
pessoas["Nome"] = "Joao" #Modifica o conteudo de nome
pessoas["Peso"] = 55.6 #Adiciona um index peso com conteudo 55.6
print(pessoas)
print("="*40)

# Dicionarios dentro de uma lista

estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "São Paulo", "Sigla": "SP"}
brasil = list()
#Adiciona os dicionarios a lista
brasil.append(estado1)
brasil.append(estado2)
# Printa a lista brasil
print(brasil)
# Printa o index 1 da lista, no caso o dicionario estado2
print(brasil[1])
# Print o index 0 da lista com elemento "UF", resulta em Rio de Janeiro
print(brasil[0]["UF"])

print("="*40)

# For com copia de dados do dicionario para lista
estado = dict()
br = list()

for c in range(0, 3):
    estado["UF"] = str(input("Digite a UF: "))
    estado["Sigla"] = str(input("Digite a sigla: "))
    br.append(estado.copy())
# Print organizado com for
for e in br:
    print(e)
print("="*40)

# Print com formatação organizada

for e in br:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")
print("="*40)

# Posso usar também:
for e in br:
    for v in e.values():
        print(v)
print("="*40)


# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = dict()

dicionario["Nome"] = str(input("Nome: "))
dicionario["Média"] = float(input("Média: "))
if dicionario["Média"] >= 7:
    dicionario["Situação"] = "Aprovado"
elif 6 <= dicionario["Média"]:
    dicionario["Situação"] = "Recuperação"
else:
    dicionario["Situação"] = "Reprovado"

print("="*40)
print(f"- Nome é igual a {dicionario['Nome']}\n"
      f"- Média é igual a {dicionario['Média']}\n"
      f"- Situação é igual a {dicionario['Situação']}")

#Posso usar também
#for k, v in dicionario.items():
    #print(f"   -{k} é igual a {y}")
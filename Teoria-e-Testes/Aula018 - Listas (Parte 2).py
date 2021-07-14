teste = list()
teste.append("Guilherme")
teste.append("20")
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = "34"
galera.append(teste[:])
print(galera)
print("="*50)


pessoal = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(pessoal[0]) #João,19
print(pessoal[0][0]) #João
print(pessoal[2][1]) #13
print("="*50)


#printar tudo
for p in pessoal:
    print(p)
print("="*50)

#printar só o nome
for p in pessoal:
    print(p[0])
print("="*50)

#printar só a idade
for p in pessoal:
    print(p[1])
print("="*50)

#print organizado
for p in pessoal:
    print(f"{p[0]} tem {p[1]} anos de idade! ")
print("="*50)

#Duas listas
galera2 = list()
dado = list()

for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera2.append(dado[:])
    dado.clear()
print(galera2)
print(dado)


# Filtrar com duas listas
totMaior = 0
totMenor = 0
for p in galera2:
    if p[1] >= 21:
        print(f"{[p[0]]} é maior de idade")
        totMaior += 1
    else:
        print(f"{[p[0]]} é menor de idade")
        totMenor += 1
print(f"Temos {totMaior} maiores e {totMenor} menores de idade")




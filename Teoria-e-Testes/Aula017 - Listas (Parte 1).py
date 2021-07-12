# Tupla --> Imutavel
#num = (2, 5, 9, 1)
# num[2] = 3 --> ERRO
#

# Lista --> Aceita mudanças de valores
num = [2, 5, 9, 1]
num[2] = 3
print(num)
# num[4] = 7 #ERRO pois não posso adicionar elementos dessa forma
num.append(7) #Adicionar elemento 7 a lista
num.sort() #Organiza por ordem
num.sort(reverse=True) #Organiza por ordem reversa
print(f"Essa lista tem {len(num)} elementos. ") #Mostra o numero de elementos da lista


num.insert(2, 0) #Insere o valor 0 na posicao 2
num.pop() #Elimina o ultimo valor
num.pop(2) #Elimina o valor da posicao 2
num.remove(2) #Remove o conteudo (apenas a primeira ocorrencia)
#num.remove(4) # Da erro pois nao esta na lista

if 4 in num:
    num.remove(4)
else:
    print("Nao achei 4 na lista")


# Outro metodo de criar listas
# valores = list(conteudo, conteudo, conteudo)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#Print organizado
for c, valor in enumerate(valores): #enumerate pega tanto a posicao quanto o valor
    print(f"Na posicao {c} encontrei o valor {valor}...")
print("FIM")

#Ler valores no teclado e colocar na lista
valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input("Digite um valor: ")))

#Testes com varias listas
a = [2, 3, 4, 7]
b = a
b[2] = 8 #mexe nas duas listas, pois ambas são iguais
print(a)
print(b)

print("================================================")
#Para copiar listas
b = a[:] # cria uma copia de a em b
b[2] = 8 #Agora a modificacao só ocorre em b
print(a)
print(b)


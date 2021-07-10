
# Sem tupla muda o conteudo da variavel
lanche = "Hamburguer"
lanche = "Suco"
# Tupla
lanche = ("Hamburger", "Suco", "Pizza", "Pudim")
print(lanche)
print(lanche[1]) #Segundo valor da tupla lanche --> Suco
print(lanche[3]) #4 valor --> Pudim
print(lanche[-2]) #Segundo valor no sentido contrario, no caso a pizza
print(lanche[1:3]) #  (suco e pizza) para em um antes do index 3
print(lanche[2:]) #Vai do index 2 ao final, no caso vai de pizza até o final
print(lanche[:2]) # do inicio até o elemento 2
print(lanche[-3:]) #começa no suco e vai até o final (hamburguer) com sentido contrario

print("===============================================================================")
#TUPLAS SÃO IMUTAVEIS

# lanche[1] = "Refrigerante"
# Esse comando resulta em erro, pois as tuplas são imutaveis

#Print usando iteração

for comida in lanche:
    print(f"Comidas disponiveis: {comida}")
print("Fim do cardápio")

print(len(lanche)) #Printa o tamanho da tupla, nesse caso 4
print("===============================================================================")

#Contador até o len da tupla, printa a posição dos lanches na tupla, igual ao anterior!
for cont in range(0, len(lanche)):
    print(lanche[cont])
print("===============================================================================")


#Os dois metodos acima estão certos, ambos podem ser utilizados conforme a necessidade

#3 metodo possivel--> Esse mostra a posição com o numero dela

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("===============================================================================")

# Mostra o dado e a posicao

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("===============================================================================")

# Printa a tupla em ordem alfabetica

print(sorted(lanche))
print("===============================================================================")

# Duas tuplas com soma

a = (2, 5, 4)
b = (5, 8, 1, 2)
#Concatena as duas tuplas a e b ao invés de soma-las
c = a + b
print(c)

print(len(c)) #Tamanho de c
print(c.count(5)) #quantas vezes o número 5 aparece em c --> 2 vezes
print(c.count(4)) #quantas vezes o número 4 aparece em c --> 1 vez
print(c.count(5)) #quantas vezes o número 5 aparece em c --> 0 vezes, por isso printa 0

print(c.index(8)) #Printa a posicao em que esta o numero 8, pode ser de 0 até o ultimo index
print(c.index(2)) # o 2 aparece 2 vezes na tupla, porém o index exibido será o da primeira ocorrencia
print(c.index(5, 1)) #printa o index do 5 contando a partir da posicao 1, ele aparece na posicao 0, porém nesse caso
# será exibido que ele aparece no index 5
print("===============================================================================")
# Uma mesma tupla aceita dados de tipos diferentes
pessoa = ("Guilherme", 20, "M", 61.40)
del(pessoa) # Apago a tupla inteira



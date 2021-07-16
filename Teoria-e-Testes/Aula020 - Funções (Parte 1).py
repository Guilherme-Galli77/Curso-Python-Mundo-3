def lin():
    print("=" * 30)


# Programa principal sem função
# print("="*30)
# print("Curso em video")
# print("="*30)
# print("="*30)
# print("Aprenda Python")
# print("="*30)
# print("="*30)
# print("Teste")
# print("="*30)


# Prograna principal com função
lin()
print("Curso em video")
lin()
print("Aprenda Python")
lin()
print("Teste")
lin()


# Funções com parametro
def mensagem(msg):
    print("=" * 30)
    print(msg)
    print("=" * 30)


mensagem("SISTEMA DE ALUNOS")


def titulo(txt):
    print("=" * 30)
    print(txt)
    print("=" * 30)


titulo("CURSO EM VIDEO")
titulo("PYTHON 3")

#####################################
print("%"*50)

# Código sem uso de função
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
print("%"*50)

# Código com uso de função


def soma(a, b):
    s = a + b
    print(s)


# Programa principal
soma(4, 2)
soma(6, 3)
# soma(4) # RESULTA EM ERRO --> SÓ RECEBE 1 PARAMETRO
# soma(3, 9, 5) # RESULTA EM ERRO --> RECEBE 3 PARAMETROS

# Outro jeito de representar os parametros (posso inverter os parametros)
soma(a=4, b=5)
soma(b=4, a=7)

print("%"*50)

# EMPACOTAR PARAMETROS


def contador(* num):
    for valor in num:
        print(f" {valor}",end="")
    print(" FIM")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print("%"*50)





# Funções e Listas


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print("%"*50)



def somaMaior(* valores3):
    s = 0
    for num in valores3:
        s += num
    print(f"Somando os valores {valores3} temos {s}")


somaMaior(5, 2)
somaMaior(2, 9, 4)
def metade(p):
    return print(f"A metade de R$ {p:.2f} é R$ {p/2:.2f}".replace(".", ","))


def dobro(p):
    return print(f"O dobro de R$ {p:.2f} é R$ {p*2:.2f}".replace(".", ","))


def aumentando(p,v):
    return print(f"Aumentando {v}%, temos R$ {p*(1+(v/100)):.2f}".replace(".", ","))


def diminuindo(p,d):
    return print(f"Diminuindo {d}%, temos R$ {p*(1-(d/100)):.2f}".replace(".", ","))

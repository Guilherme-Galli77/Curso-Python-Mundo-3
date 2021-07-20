def metade(p):
    return print(f"A metade de R$ {p:.2f} é R$ {p/2:.2f}")


def dobro(p):
    return print(f"O dobro de R$ {p:.2f} é R$ {p*2:.2f}")


def aumentando(p,v):
    return print(f"Aumentando {v}%, temos R$ {p*(1+(v/100)):.2f}")


def diminuindo(p,d):
    return print(f"Diminuindo {d}%, temos R$ {p*(1-(d/100)):.2f}")


def resumo(p, v, d):
    return print(f"================================================\n"
                 f"              RESUMO DO VALOR                   \n"
                 f"================================================\n"
                 f"Preço analisado:              R$  {p:.2f}\n"
                 f"Dobro do preço:               R$ {p*2:.2f}\n"
                 f"Metade do preço:              R$ {p/2:.2f}\n"
                 f"{v}% de aumento:              R$ {p*(1+(v/100)):.2f}\n"
                 f"{d}% de redução:              R$ {p*(1-(d/100)):.2f}\n"
                 f"================================================".replace(".",","))


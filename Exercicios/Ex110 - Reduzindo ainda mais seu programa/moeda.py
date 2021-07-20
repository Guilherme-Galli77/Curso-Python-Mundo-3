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


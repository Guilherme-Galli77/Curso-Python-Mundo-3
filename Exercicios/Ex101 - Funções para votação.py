# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def voto(a):
    from datetime import datetime
    idade = datetime.today().year - ano
    print(f"Com {idade} anos: ", end="")
    if idade < 16:
        print("VOTO NEGADO")
    elif 16 <= idade < 18 or idade > 65:
        print("VOTO OPCIONAL")
    else:
        print("VOTO OBRIGATÓRIO")


ano = int(input("Em que ano voce nasceu? "))
voto(ano)

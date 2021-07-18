# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*num, sit=False):
    """
    --> Função para analisar nota e situação de determinada turma
    :param num: Recebe uma ou mais notas
    :param sit: Habilita ou não a exibição da situação do aluno
    :return: Retorna um dicionario contendo a quantidade de notas, a maior e menor nota, a media da turma e a situação
    """
    menor = maior = c = soma = 0
    for n in num:
        soma += n
        if c == 0:
            menor = n
            maior = n
        if n < menor:
            menor = n
        if n > maior:
            maior = n
        c += 1
    media = soma / len(num)
    if media >= 6:
        s = "BOA"
    else:
        s = "RUIM"
    if sit:
        dic = {"Total": len(num), "Maior": maior, "Menor": menor, "Média": media, "Situação" : s}
    else:
        dic = {"Total": len(num), "Maior": maior, "Menor": menor, "Média": media}

    return dic


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
resp = notas(5.5, 2.5, 1.5)
print(resp)
help(notas)
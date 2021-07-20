from Ex115.lib.interface import *
from Ex115.lib.arquivo import *

from time import sleep

arq = "arquivo.txt"

if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso! ")
else:
    print("Arquivo não encontrado! ")
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        # Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO: ")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do sistema
        cabecalho("Saindo do sistema...Até logo! ")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)

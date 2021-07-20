# Exercício Python 114: Crie um código em Python que teste se o site x está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://google.com")
except:
    print("Deu erro ao acessar o site! ")
else:
    print("Site acessado com sucesso!")
    print(site.read())

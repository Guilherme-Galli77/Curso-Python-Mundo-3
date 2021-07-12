palavras = ("teste", "codigo", "programar", "casa", "livro", "python",
            "programacao", "caneta", "cachorro", "gato", "cadeira", "verde"
            "maça", "arroz")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end="")
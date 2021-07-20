try:
    a = int(input("Num: "))  # 8
    b = int(input("Denominador: "))  # 0
    r = a / b

except:
    print(f"Erro!")
else:
    print(f"resposta: {r}")  # Divisão por zero --> erro
finally:
    print("FIM DO CODIGO")

print("="*50)
# Outro formato de tratamento de exceção
try:
    a = int(input("Num: "))  # 8
    b = int(input("Denominador: "))  # 0
    r = a / b

except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(f"resposta: {r}")  # Divisão por zero --> erro
finally:
    print("FIM DO CODIGO")

print("="*50)
# Outro formato de tratamento de exceção, agora com varias exceções/erros
try:
    a = int(input("Num: "))  # 8
    b = int(input("Denominador: "))  # 0
    r = a / b

except (ValueError, TypeError):
    print(f"Problema com os tipos de dados digitados")
except ZeroDivisionError:
    print("Não é possível dividir um numero por zero ")
except KeyboardInterrupt:
    print("O usuario optou por nao informar os dados")
except Exception as erro:
    print(f"Erro encontrado foi {erro.__cause__}")
else:
    print(f"resposta: {r}")  # Divisão por zero --> erro
finally:
    print("FIM DO CODIGO")


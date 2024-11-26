lista = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir:"))
        print(lista[i])
    except ValueError as e:
        print("Digite um número!")
        raise
    finally:
        print(f"Sempre o finally é executado")

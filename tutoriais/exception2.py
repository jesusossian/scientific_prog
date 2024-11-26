lista = ["Ana","Carlos","Marta"]
for k in range(3):
    try:
        i = int(input("Digite o indice que quer imprimir:"))
        print(lista[i])
    except Exception as e:
        print(f"Algo de errado aconteceu: {e}")

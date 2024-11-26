lista = ["Ana","Carlos","Marta"]
for k in range(3):
    try:
        i = int(input("Digite o indice que quer imprimir:"))
        print(lista[i])
    except ValueError:
        print("Digite um numero!")
    except IndexError:
        print("Valor invalido, digite entre -3 e 2!")

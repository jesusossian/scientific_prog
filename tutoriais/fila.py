ultimo = 5
fila = list(range(1, ultimo+1))
print(f"fila = {fila}")

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operação == "F":
        ultimo += 1  # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")

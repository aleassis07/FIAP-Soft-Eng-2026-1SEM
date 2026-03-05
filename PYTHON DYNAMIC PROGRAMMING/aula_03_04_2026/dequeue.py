fila = ["Porto Alegre", "Florianópolis", "Curitiba"]
print(fila)
while len(fila) > 0:
    atendido = fila.pop(0)
    print("Saiu:", atendido)
    print("Fila agora:", fila)


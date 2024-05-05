

def ingresar_matriz():
    while True:
        try:
            n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
            if n <= 0:
                print("El tamaño de la matriz debe ser un entero positivo.")
                continue
            matriz = []
            print("Ingrese los elementos de la matriz:")
            for i in range(n):
                fila = []
                for j in range(n):
                    while True: 
                        entrada = int(input(f"Elemento [{i+1},{j+1}]: "))
                        if entrada >= 0 and entrada <= 1:
                            fila.append(entrada)
                            break
                        else:
                            print("Ingrese un valor valido")
                matriz.append(fila)
            return np.array(matriz)
        except ValueError:
            print("Por favor, ingrese un número válido para los elementos de la matriz.")

def mostrar_relaciones(matriz):
    relaciones = []
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                relaciones.append((i+1, j+1))
    print("Relaciones generadas por la matriz:")
    for rel in relaciones:
        print(f"R({rel[0]},{rel[1]})")

def validar_propiedades(matriz):
    # Verificar reflexividad
    reflexivo = all(matriz[i][i] == 1 for i in range(len(matriz)))

    # Verificar simetría
    simetrico = all(matriz[i][j] == matriz[j][i] for i in range(len(matriz)) for j in range(len(matriz)))

    # Verificar transitividad
    transitivo = all(matriz[i][j] == 1 and matriz[j][k] == 1 <= matriz[i][k] for i in range(len(matriz)) for j in range(len(matriz)) for k in range(len(matriz)))

    # Verificar antisimetría
    antisimetrico = all(matriz[i][j] == 1 and matriz[j][i] == 1 <= (i == j) for i in range(len(matriz)) for j in range(len(matriz)))

    print("Propiedades de la matriz:")
    print("Reflexividad:", reflexivo)
    print("Simetría:", simetrico)
    print("Transitividad:", transitivo)
    print("Antisimetría:", antisimetrico)

def generar_grafo(matriz):
    G = nx.DiGraph()
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                G.add_edge(i+1, j+1)
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, arrowsize=20)
    plt.title("Grafo Dirigido basado en la matriz original")
    plt.show()

def main():
    matriz = ingresar_matriz()
    print("Matriz ingresada:")
    print(matriz)
    mostrar_relaciones(matriz)
    validar_propiedades(matriz)
    generar_grafo(matriz)

if __name__ == "__main__":
    main()
0

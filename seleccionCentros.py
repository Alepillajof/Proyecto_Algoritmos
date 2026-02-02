def leerCentrosDisponibles():
    centros = []

    try:
        with open("centros.txt", "r") as archivo:
            for linea in archivo:
                centro = linea.strip()
                if centro != "":
                    centros.append(centro)

    except FileNotFoundError:
        print("Error: No se encontro el archivo centros .txt")
    
    return centros

def agregarCentro(centrosSeleccionados, centro):
    if centro in centrosSeleccionados:
        print("El centro ya fue seleccionado")
    else:
        print("Centro agregado correctamente")

def eliminarCentro(centrosSeleccionados, centro):
    if centro in centrosSeleccionados:
        centrosSeleccionados.remove(centro)
        print("Centro eliminado")
    else:
        print("El centro no esta en la seleccion")

def mostrarCentros(centrosSeleccionados):
    if not centrosSeleccionados:
        print("No hay centros seleccionados")
    else:
        print("Centros seleccionados:")
        for i, centro in enumerate(centrosSeleccionados, start=1):
            print(f"{i}. {centro}")

def ordenarCentros(centrosSeleccionados):
    n = len(centrosSeleccionados)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if centrosSeleccionados[j] > centrosSeleccionados[j + 1]:
                aux = centrosSeleccionados[j]
                centrosSeleccionados[j] = centrosSeleccionados[j + 1]
                centrosSeleccionados[j + 1] = aux

    print("Centros ordenados correctamente\n");

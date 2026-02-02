def guardarRutas(nombreCliente, centrosSeleccionados):
    nombreArchivo = f"rutas-{nombreCliente}.txt"

    with open(nombreArchivo, "w") as archivo:
        archivo.write("Centros seleccionados:\n")
        for centro in centrosSeleccionados:
            archivo.write(centro + "\n")


    print(f"Rutas guardadaes en {nombreArchivo}")

    
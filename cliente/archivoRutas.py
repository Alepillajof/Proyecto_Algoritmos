import os

def guardarRutas(nombreCliente, centrosSeleccionados):
    rutaCarpeta = "cliente"
    nombreArchivo = f"rutas-{nombreCliente}.txt"
    rutaCompleta = os.path.join(rutaCarpeta, nombreArchivo)

    with open(nombreArchivo, "w") as archivo:
        archivo.write("Centros seleccionados:\n")
        for centro in centrosSeleccionados:
            archivo.write(centro + "\n")


    print(f"Rutas guardadaes en {rutaCompleta}")


    

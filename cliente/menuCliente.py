from cliente.arbolRegiones import construirArbolRegiones, mostrarArbol

from cliente.seleccionCentros import (leerCentrosDisponibles, agregarCentro, eliminarCentro, mostrarCentros, ordenarCentros)

from cliente.archivoRutas import guardarRutas

# SUB MENU
def menuSeleccionCentros(centrosSeleccionados, nombreCliente):

    while True:
        print("\n=== SELECCION DE CENTROS ===")
        print("1. Agregar centro")
        print("2. Eliminar centro")
        print("3. Ver centros seleccionados")
        print("4. Ordenar centros seleccionados")
        print("5. Guardar y volver")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Error: Ingrese un numero\n")
            continue

        match opcion:
            case 1:
                centros = leerCentrosDisponibles()
                for i, c in enumerate(centros, start=1):
                    print(f"{i}. {c}")

                try:
                    op = int(input("Seleccione centro: "))
                    centroElegido = centros[op - 1]
                    agregarCentro(centrosSeleccionados, centroElegido)
                except:
                    print("Seleccion invalida")

            case 2:
                mostrarCentros(centrosSeleccionados)
                if centrosSeleccionados:
                    centro = input("Centro a eliminar: ")
                    eliminarCentro(centrosSeleccionados, centro)

            case 3:
                mostrarCentros(centrosSeleccionados)

            case 4:
                ordenarCentros(centrosSeleccionados)

            case 5:
                guardarRutas(nombreCliente, centrosSeleccionados)
                break
            case _:
                print("Opcion invalida\n")


def menuCliente(nombreCliente):
    centrosSeleccionados = []

    while True:
        print("\n=== MENU CLIENTE ===")
        print("1. Ver mapa de centros conectados")
        print("2. Consultar ruta optima y costo")
        print("3. Explorar centros por regiones")
        print("4. Seleccionar centros para envio")
        print("5. Salir")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Error: Ingrese un numero\n")
            continue

        match opcion:
            case 1:
                print("\n=== MAPA DE CENTROS CONECTADOS ===")
                
            case 2:
                print("\n=== RUTA OPTIMA ===")
                
            case 3:
                print("\n=== CENTRO POR REGIONES ===")
                arbol = construirArbolRegiones()
                mostrarArbol(arbol)

            case 4:
                menuSeleccionCentros(centrosSeleccionados, nombreCliente)
                
            case 5:
                print("Saliendo del menu cliente...")
                break
            case _:
                print("Opcion invalida\n")

from cliente.arbolRegiones import construirArbolRegiones, mostrarArbol

def menuCliente(nombreCliente):
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
                print("\n=== CENTROS PARA ENVIO ===")
                
            case 5:
                print("Saliendo del menu cliente...")
                break
            case _:
                print("Opcion invalida\n")

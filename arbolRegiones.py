def construirArbolRegiones():
    arbol = {
        "Ecuador": {
            "Sierra": ["Quito", "Ambato", "Latacunga"],
            "Costa": ["Guayaquil", "Manta"],
            "Amazonia": ["Tena", "Puyo"]
        }
    }
    return arbol

def mostrarArbol(arbol):
    print("Ecuador")

    regiones = arbol["Ecuador"]

    for region in regiones:
        print(" -", region)

        centros = regiones[region]

        for centro in centros:
            print("     -", centro)


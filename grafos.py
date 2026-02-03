import heapq

# =========================
# GRAFO DE CENTROS
# =========================

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_centro(self, centro):
        if centro not in self.grafo:
            self.grafo[centro] = []

    def agregar_ruta(self, origen, destino, costo):
        self.agregar_centro(origen)
        self.agregar_centro(destino)
        self.grafo[origen].append((destino, costo))
        self.grafo[destino].append((origen, costo))  # bidireccional

    def mostrar_grafo(self):
        for centro in self.grafo:
            print(f"{centro} → {self.grafo[centro]}")

# =========================
# MATRIZ DE COSTOS
# =========================

def matriz_costos(grafo):
    centros = list(grafo.grafo.keys())
    n = len(centros)
    matriz = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        matriz[i][i] = 0

    for i, origen in enumerate(centros):
        for destino, costo in grafo.grafo[origen]:
            j = centros.index(destino)
            matriz[i][j] = costo

    return centros, matriz

# =========================
# DIJKSTRA CON HEAP
# =========================

def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('inf') for nodo in grafo.grafo}
    distancias[inicio] = 0
    anteriores = {}

    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual == fin:
            break

        for vecino, costo in grafo.grafo[nodo_actual]:
            nueva_distancia = distancia_actual + costo
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    ruta = []
    actual = fin
    while actual in anteriores:
        ruta.insert(0, actual)
        actual = anteriores[actual]
    ruta.insert(0, inicio)

    return ruta, distancias[fin]

# =========================
# BFS
# =========================

def bfs(grafo, inicio):
    visitados = set()
    cola = [inicio]
    resultado = []

    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
            resultado.append(nodo)
            for vecino, _ in grafo.grafo[nodo]:
                cola.append(vecino)

    return resultado

# =========================
# DFS
# =========================

def dfs(grafo, inicio, visitados=None, resultado=None):
    if visitados is None:
        visitados = set()
    if resultado is None:
        resultado = []

    visitados.add(inicio)
    resultado.append(inicio)

    for vecino, _ in grafo.grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados, resultado)

    return resultado

# =========================
# PRUEBA DEL SISTEMA
# =========================

if __name__ == "__main__":
    g = Grafo()
    g.agregar_ruta("Centro A", "Centro B", 10)
    g.agregar_ruta("Centro B", "Centro C", 5)
    g.agregar_ruta("Centro A", "Centro C", 20)
    g.agregar_ruta("Centro C", "Centro D", 8)

    print("GRAFO:")
    g.mostrar_grafo()

    print("\nDIJKSTRA:")
    ruta, costo = dijkstra(g, "Centro A", "Centro D")
    print("Ruta:", ruta)
    print("Costo total:", costo)

    print("\nBFS:", bfs(g, "Centro A"))
    print("DFS:", dfs(g, "Centro A"))

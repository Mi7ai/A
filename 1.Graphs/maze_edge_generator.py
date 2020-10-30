from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
import random
from labyrinthviewer import LabyrinthViewer
from typing import *

"""
empezar en (0,0)
recorrer cada vecino de (0,0) que son 4. tener en cuenta no salirse del tamano del laberinto (filas x columnas)
para cada vecino hacer un recorrido en profundidad. probar con anchura tambien.
tener una lista de aristas para anadir los vertices asi tengo en cuenta donde estan las paredes
"""
Vertex = TypeVar('Vertex')
f = 3
c = 3


# metodo que genera todos los vertices vecinos de un vertice "u" a los que puede ir
def vecinos_vertice(u: Vertex):
    vertices_vecinos = []
    fila, columna = u
    seen = []
    random.seed(7)
    choice = random.randint(0, 3)

    if fila - 1 >= 0:  # si voy al norte
        vecino = (fila - 1, columna)
        if vecino not in seen:
            vertices_vecinos.append(vecino)
    if columna + 1 < c:  # si voy al este
        vecino = (fila, columna + 1)
        if vecino not in seen:
            vertices_vecinos.append(vecino)
    if fila + 1 < f:  # si voy al sur
        vecino = (fila + 1, columna)
        if vecino not in seen:
            vertices_vecinos.append(vecino)
    if columna - 1 >= 0:  # si voy al oeste
        vecino = (fila, columna - 1)
        if vecino not in seen:
            vertices_vecinos.append(vecino)

    return vertices_vecinos


def generar_aristas_profundidad(u, v):
    seen = set()
    aristas = []
    random.seed(5)

    def explorar_desde(u, v):
        seen.add(v)
        aristas.append((u, v))
        # hacer un shuffle del vecino que voy a coger. no hace falta realmente
        vecinos = vecinos_vertice(v)
        random.shuffle(vecinos)
        for suc in vecinos:
            if suc not in seen:
                explorar_desde(v, suc)

    explorar_desde(v_ini, v_ini)
    return aristas


def gernerar_aristas_anchura(v_ini):
    q = Fifo()
    seen = set()
    aristas = []

    q.push((v_ini, v_ini))
    seen.add(v_ini)

    while len(q) > 0:
        (u, v) = q.pop()
        aristas.append((u, v))

        for suc in vecinos_vertice(v):
            if suc not in seen:
                seen.add(suc)
                q.push((v, suc))

    return aristas


def generate(f, c):
    aristas = []
    v_ini = (1, 1)
    aristas.append((v_ini, v_ini))
    seen = set()

    for i in range(f):
        for j in range(c):
            x = random.randint(0, f)
            y = random.randint(0, c)
            aristas.append((x, y))
    return aristas


if __name__ == '__main__':
    # aristas = generate(2, 2)
    # print(aristas)
    v_ini = (0, 0)
    print(vecinos_vertice(v_ini))
    # print(generar_aristas_profundidad(v_ini, v_ini))
    pasillos_profundidad = generar_aristas_profundidad(v_ini, v_ini)

    # pasillos_anchura = gernerar_aristas_anchura(v_ini)

    lab = UndirectedGraph(E=pasillos_profundidad)
    lv = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)
    lv.run()

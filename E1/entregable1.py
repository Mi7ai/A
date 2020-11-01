import sys

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
import random
from labyrinthviewer import LabyrinthViewer
from typing import *
from algoritmia.datastructures.mergefindsets import MergeFindSet

"""
empezar en (0,0)
recorrer cada vecino de (0,0) que son 4. tener en cuenta no salirse del tamano del laberinto (filas x columnas)
para cada vecino hacer un recorrido en profundidad. probar con anchura tambien.
tener una lista de aristas para anadir los vertices asi tengo en cuenta donde estan las paredes
"""
Vertex = TypeVar('Vertex')
f = 2
c = 2
filename = sys.argv[1]


def load_file(filename):
    aristas = []

    try:
        f = open(filename, "r")
        filas, columnas = f.readline().split(" ")

        paredes = f.readline()

        for line in f:
            x1, y1, x2, y2 = line.split(" ")
            vertice1 = (int(x1), int(y1))
            vertice2 = (int(x2), int(y2))
            arista = (vertice1, vertice2)

            aristas.append(arista)
    except IOError:
        print("File cannot be open!")

    return int(filas), int(columnas), int(paredes), aristas


def create_labyrinth(rows, cols):
    # general expressions of all vertexes
    vertices = [(row, col) for row in range(rows) for col in range(cols)]

    mfs = MergeFindSet()
    edges = []

    for v in vertices:
        mfs.add(v)

    # add the bottom row and right column to edge list and shuffle it
    for row, col in vertices:
        if row + 1 < rows:
            edges.append([(row, col), (row + 1, col)])
        if col + 1 < cols:
            edges.append([(row, col), (row, col + 1)])
    random.shuffle(edges)

    corridors = []

    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return UndirectedGraph(E=corridors)


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

    random.seed(86)

    def explorar_desde(u, v):
        seen.add(v)
        aristas.append((u, v))
        # hacer un shuffle del vecino que voy a coger. no hace falta realmente
        vecinos = vecinos_vertice(v)
        random_vecinos = random.sample(vecinos, len(vecinos))
        print("Vecinos de{0} {1} y random {2}".format(v, vecinos, random_vecinos))
        # a = sorted(vecinos, key=lambda i: vecinos[i])
        # print(a)
        for i in range(len(random_vecinos)):
            suc = random_vecinos[random.randint(0, len(random_vecinos) - 1)]
            if suc not in seen:
                explorar_desde(v, suc)

    explorar_desde(v_ini, v_ini)
    return aristas


def generar_aristas_anchura(v_ini):
    q = Fifo()
    seen = set()
    aristas = []
    random.seed(3)

    q.push((v_ini, v_ini))
    seen.add(v_ini)

    while len(q) > 0:
        (u, v) = q.pop()
        aristas.append((u, v))

        vecinos = list(vecinos_vertice(v))

        random_vecinos = random.sample(vecinos, len(vecinos))
        # print("Vecinos de{0} {1} y random {2}".format(v,vecinos,random_vecinos))
        for suc in random_vecinos:
            if suc not in seen:
                seen.add(suc)
                q.push((v, suc))

    return aristas


if __name__ == '__main__':
    # aristas = generate(2, 2)
    # print(aristas)
    v_ini = (0, 0)
    # print(vecinos_vertice(v_ini))
    # print(generar_aristas_profundidad(v_ini, v_ini))

    # pasillos_profundidad = generar_aristas_profundidad(v_ini, v_ini)
    # pasillos_profundidad_copy = generar_aristas_profundidad_copy(v_ini, v_ini)
    # pasillos_anchura = gernerar_aristas_anchura(v_ini)
    # pasillos_anchura_copy = generar_aristas_anchura_copy(v_ini)
    # print(pasillos_profundidad)

    # lab = UndirectedGraph(E=pasillos_profundidad)
    # lab = UndirectedGraph(E=pasillos_profundidad_copy)
    # lab = UndirectedGraph(E=pasillos_anchura)

    filas, columnas, paredes, aristas_p = load_file(filename)

    lab = create_labyrinth(filas, columnas)
    lv = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)
    lv.run()

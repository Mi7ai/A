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
    np = []
    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        if (u, v) not in aristas_p:
            if mfs.find(u) != mfs.find(v):
                mfs.merge(u, v)
                corridors.append((u, v))
        # else:
        #     np.append((u,v))

    # print(len(np))
    # for u, v in corridors:
    #     print("Path: {} {}".format(u, v))
    return corridors,UndirectedGraph(E=corridors)


if __name__ == '__main__':
    filas, columnas, paredes, aristas_p = load_file(filename)

    c, lab = create_labyrinth(filas, columnas)

    # for u,v in c:
    #     if (u, v) in aristas_p:
    #         print("Hay", (u,v))



    lv = LabyrinthViewer(lab, canvas_width=1000, canvas_height=1000, margin=10)

    lv.add_marked_cell(aristas_p[0][0], 'blue')
    lv.add_marked_cell(aristas_p[0][1], 'blue')
    lv.run()

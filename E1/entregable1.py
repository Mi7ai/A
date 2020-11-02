from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from labyrinthviewer import LabyrinthViewer
import time
import sys
import random
from typing import *

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
    paredes_p = 0
    for u, v in aristas_p:
        edges.remove([u, v])
        paredes_p += 1

    corridors = []

    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        # if (u, v) not in aristas_p:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        else:
            paredes_p -= 1

    return corridors, paredes_p, UndirectedGraph(E=corridors)


def pintar():
    for pu, pv in aristas_p:
        lv.add_marked_cell(pu, 'cyan')
        lv.add_marked_cell(pv, 'yellow')


if __name__ == '__main__':
    filas, columnas, paredes, aristas_p = load_file(filename)
    # ---
    s = time.time()
    aristas, paredes_p, lab = create_labyrinth(filas, columnas)
    e = time.time()
    print(e - s)
    # ---
    print(paredes_p)
    print(paredes)
    if paredes_p > 0:
        print(filas, columnas)
        print(len(aristas))
        for u, v in aristas:
            pass
            # print(u[0], u[1], v[0], v[1])
    else:
        print("NO ES POSIBLE CONSTRUIR EL LABERINTO")

    lv = LabyrinthViewer(lab, canvas_width=1000, canvas_height=1000, margin=10)
    # pintar()
    lv.run()

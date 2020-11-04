from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from labyrinthviewer import LabyrinthViewer
from typing import *
import random
import time
import sys

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
            edges.append(((row, col), (row + 1, col)))
        if col + 1 < cols:
            edges.append(((row, col), (row, col + 1)))

    # descartar las paredes prohibidas de edges
    edges = list(set(edges) - set(aristas_p))
    random.shuffle(edges)

    corridors = []

    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return corridors


def pintar():
    for pu, pv in aristas_p:
        lv.add_marked_cell(pu, 'cyan')
        lv.add_marked_cell(pv, 'yellow')


if __name__ == '__main__':
    random.seed(42)
    filas, columnas, paredes, aristas_p = load_file(filename)
    aristas = create_labyrinth(filas, columnas)
    # ---
    s = time.time()
    e = time.time()
    print(e - s)

    if len(sys.argv) == 3 and sys.argv[2] == "-g":
        lab = UndirectedGraph(E=aristas)
        lv = LabyrinthViewer(lab, canvas_width=1300, canvas_height=1300, margin=10)
        # pintar()
        lv.run()
        # QUITAR lo de abajo
        print(filas, columnas)
        print(len(aristas))
        # for u,v in aristas:
        #     print(u,v)
    else:
        print(filas, columnas)
        print(len(aristas))
        # for u,v in aristas:
        #     print(u,v)

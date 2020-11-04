from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from labyrinthviewer import LabyrinthViewer
import time
import sys
import random
from typing import *
import itertools

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

    random.shuffle(edges)
    # descartar las paredes prohibidas de edges
    edges = list(set(edges)-set(aristas_p))

    #---
    corridors = []

    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        # if (u, v) not in aristas_p and (v, u) not in aristas_p:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))


    # return corridors, n, UndirectedGraph(E=corridors)
    return corridors


# def crear_aristas_buenas(rows, cols, aristas_p, aristas_atm):
#     # print(list(aristas_p))
#     # print(aristas_atm)
#     aristas_f = []
#     out1 = []
#     vertices = [(row, col) for row in range(rows) for col in range(cols)]
#     edges = []
#
#     for row, col in vertices:
#         if row + 1 < rows:
#             edges.append([(row, col), (row + 1, col)])
#         if col + 1 < cols:
#             edges.append([(row, col), (row, col + 1)])
#
#     for u, v in aristas_p:
#         out1.append((u, v))
#         # out1.append((v, u))
#     print(sorted(aristas_atm))
#     print(sorted(out1))
#     a = set(out1)
#     b = set(aristas_atm)
#     print(sorted(b-a))
#
#
#     return b-a


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
    # ---
    print("---")
    print(filas, columnas)
    # print(len(aristas))
    print("---")

    lab = UndirectedGraph(E=aristas)
    lv = LabyrinthViewer(lab, canvas_width=1300, canvas_height=1300, margin=10)
    # pintar()
    lv.run()

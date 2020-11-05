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

    # for u, v in edges:
    #     if (u,v) in aristas_p:
    #         edges.remove((u,v))
    #     if (v,u) in aristas_p:
    #         edges.remove((v, u))
    print(len(edges))

    edges = list(set(edges) - set(aristas_p))

    random.shuffle(edges)

    corridors = []
    print(len(edges))
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
    print(len(corridors))
    return corridors


def pintar():
    for pu, pv in aristas_p:
        lv.add_marked_cell(pu, 'cyan')
        lv.add_marked_cell(pv, 'yellow')

def bien_formado2(aristas, aristas_p):
    for u, v in aristas:
        if (u,v) in aristas_p:
             return False
    return True

def bien_formado(lab, prohibidas):
    c = 0
    for u, v in lab.E:
        if (u, v) in prohibidas:
            c += 1
    return c


if __name__ == '__main__':
    random.seed(42)
    filas, columnas, paredes, aristas_p = load_file(filename)
    aristas = create_labyrinth(filas, columnas)
    # ---
    s = time.time()
    lab = UndirectedGraph(E=aristas)
    e = time.time()
    print(e - s)
    print()

    print("---")
    print("nr aristas:", len(lab.E))
    print("nr vertices:", len(lab.V))

    if len(sys.argv) == 3 and sys.argv[2] == "-g":

        # QUITAR lo de abajo
        print(filas, columnas)
        print(len(aristas))
        # for u,v in aristas:
        #     print(u,v)
        lv = LabyrinthViewer(lab, canvas_width=1300, canvas_height=1300, margin=10)
        # pintar()
        lv.run()
    else:
        if len(lab.E) - (len(lab.V)-1) == 0:
            print(filas, columnas)
            print(len(aristas))
            for u, v in lab.E:
                print(u[0], u[1], v[0], v[1])
        else:
            print("NO ES POSIBLE CONSTRUIR EL LABERINTO")

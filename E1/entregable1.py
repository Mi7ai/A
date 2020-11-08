from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from labyrinthviewer import LabyrinthViewer
from typing import *
import random
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
    # generar vertices
    vertices = [(row, col) for row in range(rows) for col in range(cols)]

    mfs = MergeFindSet()
    edges = []

    for v in vertices:
        mfs.add(v)

    # anadir la fila de abajo y la columna derecha a la lista de aristas y barajarla
    for row, col in vertices:
        if row + 1 < rows:
            edges.append(((row, col), (row + 1, col)))
        if col + 1 < cols:
            edges.append(((row, col), (row, col + 1)))

    # borrar las aristas prohibidas
    edges = list(set(edges) - set(aristas_p))

    random.shuffle(edges)

    corridors = []

    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return corridors, vertices


def bien_formado(lab, vertices):
    return True if len(lab.E) == len(vertices) - 1 else False


if __name__ == '__main__':
    random.seed(18)
    filas, columnas, paredes, aristas_p = load_file(filename)
    aristas, vertices = create_labyrinth(filas, columnas)

    lab = UndirectedGraph(E=aristas)

    if len(sys.argv) == 3 and sys.argv[2] == "-g":

        print(filas, columnas)
        print(len(aristas))
        for u, v in lab.E:
            print(u[0], u[1], v[0], v[1])
        lv = LabyrinthViewer(lab, canvas_width=1300, canvas_height=1300, margin=10)
        lv.run()
    else:
        if bien_formado(lab, vertices):
            print(filas, columnas)
            print(len(aristas))
            for u, v in lab.E:
                print(u[0], u[1], v[0], v[1])
        else:
            print("NO ES POSIBLE CONSTRUIR EL LABERINTO")

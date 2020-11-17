from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from typing import *
import sys
import math

Vertex = TypeVar('Vertex')

"""
objetivo: obtener ciclos hamiltonianos de longitud minima
que cono es un ciclo hamiltoniano: ir de un vertice a todos los demas formando un camino y que el ultimo enlace con el 
primero
"""


def load_file():
    nr_puntos = 0
    puntos = []

    try:
        nr_puntos = sys.stdin.readline()

        for line in sys.stdin.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)
    except IOError:
        print("File cannot be open!")
    return nr_puntos, puntos


def load_file2():
    nr_puntos = 0
    puntos = []

    try:
        f = open(sys.argv[1])
        nr_puntos = f.readline()

        for line in f.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)
    except IOError:
        print("File cannot be open!")
    return int(nr_puntos), puntos


def create_graph(puntos):
    aristas = dict()

    for v in range(len(puntos)):
        for w in range(len(puntos)):
            if v != w:
                weight = euclidean_distance(puntos[v], puntos[w])
                aristas[(v, w)] = weight
                # aristas[(w, v)] = weight

    return aristas


def euclidean_distance(x, y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]

    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


"""algoritmo kruskal
Ordenar todas las aristas en orden creciente de su peso.
elegir una arista, mirar si tiene ciclo con el spanning tree formado hasta el momento. Si no tiene ciclo, 
hacer un merge y sacar los vertices, si tiene, descartar la arista y pasar a la siguiente
repetir hasta V-1 aristas en el spt"""

"""
REQUISITO:
el segundo elemento de la lista que representa el camino será el vértice de menor índice entre los dos sucesores 
del vértice 0
"""

# TODO: finish implementation or getting the second vertex of path index 2
def min_vertex(g: UndirectedGraph, v):
     for suc in sorted(g.succs(v)):

        yield suc




def kruskal(aristas, g):
    path = []
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])
    mfs = MergeFindSet()
    distance = 0

    for v in g.V:
        # a = set()
        # a.add(v)
        mfs.add(v)
    # orden(aristas_ordenadas)

    for edge, w in aristas_ordenadas:
        u = edge[0]
        v = edge[1]
        if mfs.find(u) != mfs.find(v):
            if len(path) == 0:

                distance += w
                path.append(u)
                path.append(v)  # segundo vertice
# ---- stuck here
                vertice_a_elegir = next(min_vertex(g, v))
                print( vertice_a_elegir)
                while  vertice_a_elegir  == u:
                    vertice_a_elegir = next(min_vertex(g, v))
                mfs.merge(u, vertice_a_elegir)
                # print(u, v, "not a cicle")
# ----
            else:
                mfs.merge(u, v)
                if u not in path:
                    path.append(u)
                    distance += w
                if v not in path:
                    path.append(v)
                    distance += w
                # print(u, v, "not a cicle")

        # else:
        # print("yes a cycle")
    print(distance)

    return path


def orden(aristas_ordenadas):
    for e, w in aristas_ordenadas:
        print(e, w)


if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    aristas = create_graph(puntos)

    g = UndirectedGraph(E=aristas.keys())
    # print(g.V)
    # print(g.E)
    kruskal_path = kruskal(aristas, g)
    print(kruskal_path)

    print(min_vertex(g, 0))

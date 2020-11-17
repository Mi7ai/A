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


# algoritmo kruskal
# Ordenar todas las aristas en orden creciente de su peso.
# elegir el vertice mas pequeno. mirar si tiene ciclo con el spanning tree formado hasta el momento. Si no tiene ciclo, incluirlo en spanning tree, si tiene, descartarlo
# repetir paso anterior hasta V-1 aristas en el spt

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


# TODO: implementar esto
# es un ciclo entre el set y una arista
def is_cycle(s: MergeFindSet, u, v):
    if s.find(u) == s.find(v):
        return True
    s.merge(u, v)
    return False


def kruskal(aristas, g):
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])
    mfs = MergeFindSet()
    mst = set()
    distance = 0

    for v in g.V:
        # a = set()
        # a.add(v)
        mfs.add(v)
    print(mfs)
    orden(aristas_ordenadas)

    for edge, w in aristas_ordenadas:
        u = edge[0]
        v = edge[1]
        if mfs.find(u) != mfs.find(v):
            if len(mst) == 0:
                mfs.merge(u, v)
                distance += w
                # mst.union([u])
                # mst.append(u)
                # mst.append(v)
                print(u,v ,"not a cicle")
            else:
                mfs.merge(u, v)
                print(u, v, "not a cicle")
                distance += w
        else:
            print("yes a cycle")
    print(distance)
    print(mfs)

    # dis_set = []
    # for v in g.V:
    #     a = set()
    #     a.add(v)
    #     dis_set.append(a)


    return mst


def orden(aristas_ordenadas):
    for e, w in aristas_ordenadas:
        print(e, w)


if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    aristas = create_graph(puntos)

    g = UndirectedGraph(E=aristas.keys())
    # print(g.V)
    # print(g.E)
    k = kruskal(aristas, g)
    print(k)

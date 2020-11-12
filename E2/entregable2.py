from algoritmia.datastructures.digraphs import UndirectedGraph
import sys
import math

from algoritmia.datastructures.mergefindsets import MergeFindSet

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
    vert = set()

    # mfs = MergeFindSet()
    # for v in range(len(puntos)):
    #     mfs.add(puntos[v])

    vertices = []
    for v in range(len(puntos)):
        for w in range(len(puntos)):
            # if v != w:
            weight = distancia_euclidea(puntos[v], puntos[w])
            aristas[(v, w)] = weight
            aristas[(w, v)] = weight
    return aristas


def distancia_euclidea(x, y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]

    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    aristas = create_graph(puntos)
    print(aristas)
    x = puntos[0]
    y = puntos[1]
    print()
    print(aristas)
    g = UndirectedGraph(E=aristas.keys())
    print(g.E)


from algoritmia.datastructures.digraphs import UndirectedGraph
import sys

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
# Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
# elegir el vertice mas pequeno. mirar si tiene ciclo con el spanning tree formado hasta el momento. Si no tiene ciclo, incluirlo en spanning tree, si tiene, descartarlo
# repetir paso anterior hasta V-1 aristas en el spt

def create_graph(puntos):
    # vertices = []
    mfs = MergeFindSet()
    for v in range(len(puntos)):
        mfs.add(puntos[v])

    vertices = []
    for v in range(len(puntos)):
        for w in range(len(puntos)):
            if v != w:
                vertices.append((v, w))



    return vertices


if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    vertices = create_graph(puntos)
    print(vertices)

    g = UndirectedGraph(V=vertices)


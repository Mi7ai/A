from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from algoritmia.datastructures.mergefindsets import MergeFindSet
from typing import *
import sys
import math

from algoritmia.datastructures.queues import Fifo
from algoritmia.utils import infinity

Vertex = TypeVar('Vertex')


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


def create_graph2(puntos):
    aristas = []
    for v in range(len(puntos)):
        for w in range(len(puntos)):
            if v != w:
                weight = euclidean_distance(puntos[v], puntos[w])
                aristas.append(((v, w), weight))
    print("Create graph 2")
    print(aristas)
    return aristas


def create_graph(puntos):
    aristas = dict()
    # aristas_con_peso = []
    aristas_buenas = []

    for v in range(len(puntos)):
        for w in range(len(puntos)):
            if v != w:
                weight = euclidean_distance(puntos[v], puntos[w])
                aristas[(v, w)] = weight
                # aristas_con_peso.append(((v,w),weight))
    ini = 0
    fin = len(puntos)
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])

    limite = [2] * len(puntos)
    # limite[0] = 1
    # limite[len(puntos) - 1] = 1
    # print(limite)

    for i in range(0,len(aristas_ordenadas),2):
        edge = aristas_ordenadas[i][0]
        w = aristas_ordenadas[i][1]
        vertice1 = edge[0]
        vertice2 = edge[1]

        if limite[vertice1] > 0 and limite[vertice2] > 0:
                limite[vertice1] -= 1
                limite[vertice2] -= 1
                aristas_buenas.append((edge, w))
        # if limite[vertice1] > 0 and limite[vertice2] > 0:
        #     if vertice1 == ini and limite[vertice1] > 0:
        #         aristas_buenas.append((edge, w))
        #         limite[vertice1] -= 1
        #     elif vertice2 == fin and limite[vertice2] > 0:
        #         aristas_buenas.append((edge, w))
        #     else:
        #         aristas_buenas.append((edge, w))
        #         limite[vertice1] -= 1
        #         limite[vertice2] -= 1

    return aristas, aristas_buenas


# Todo: se puede mejorar quitando los argumentos del principio
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
el segundo elemento de la lista que representa el camino será el vértice de menor índice entre los sucesores 
del vértice 0
"""


# de entre todas las aristas no visitadas escoge la mas corta

def shortest_edge(aristas, u, v):
    lista_vertices_vecinos = g.succs(u)
    min_distance = infinity
    vertice_menor = v
    for vecino in lista_vertices_vecinos:
        if vecino != v:
            if aristas[u, vecino] < min_distance:
                min_distance = aristas[u, vecino]
                vertice_menor = vecino

    # print(vertice_menor)
    return vertice_menor

def kruskal2(aristas):
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])
    mfs = MergeFindSet()
    limite = [2] * len(puntos)
    path = []
    for v in range(len(puntos)):
        mfs.add(v)

    for edge, w in aristas_ordenadas:
        u = edge[0]
        v = edge[1]

        if limite[u] > 0 and limite[v] > 0: #puedo meter la arista si no tiene ciclo
            if mfs.find(u) != mfs.find(v): #no hace ciclo

                mfs.merge(u, v)
                path.append(edge)
                limite[u] -= 1
                limite[v] -= 1
    vertice_extra = []
    for i, x in enumerate(limite):
        if x==1:
            vertice_extra.append(i)
    print(tuple(vertice_extra))
    path.append(tuple(vertice_extra))
    return path

def kruskal(aristas, g):
    path = []
    aristas_ordenadas = sorted(aristas.items(), key=lambda x: x[1])
    mfs = MergeFindSet()
    distance = 0

    for v in g.V:
        mfs.add(v)
    # PRINT
    # orden(aristas_ordenadas)

    # PRINT
    # sa = sorted(g.E, key=lambda i: aristas[i])
    # print(sa)

    for edge in sorted(g.E, key=lambda i: aristas[i]):
        u = edge[0]
        v = edge[1]
        if len(path) == len(g.V):
            break

        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            # if len(path) == 0:
            #
            #     path.append(u)  # vertice a mirar
            #     vertice_a_elegir = shortest_edge(aristas, u, v)
            #     if vertice_a_elegir != v:
            #         path.append(vertice_a_elegir)
            #     mfs.merge(u, vertice_a_elegir)
            #     # distance += aristas[u, vertice_a_elegir]
            #
            # else:
            #     mfs.merge(u, v)
            #     if u not in path:
            #         path.append(u)
            #         # distance += w
            #     if v not in path:
            #         path.append(v)
            #         # distance += w

    print("Distancia", distance)
    # print(aristas_ordenadas)
    return path


def orden(aristas_ordenadas):
    print("Aristas ordenadas")
    for e, w in aristas_ordenadas:
        print(e, w)


def check_distance(aristas, path):
    # path = [0, 1, 4, 3, 2]
    total = 0
    for i in range(len(path) - 1):
        total += aristas[path[i], path[i + 1]]
        print("De {} a {} = {}. Acumulado = {}".format(path[i], path[i + 1], (aristas[path[i], path[i + 1]]), total))
    print("Distancia total del camino = {}".format(total))

def kruskal_final(g, v_ini, aristas):
    q = Fifo()
    seen = set()
    vertices = []

    # q.push(v_ini)
    seen.add(v_ini)

    vertices.append(v_ini)
    sucs = g.succs(v_ini)

    vecino1 = sucs.pop()
    vecino2 = sucs.pop()

    if aristas[(v_ini,vecino1)] < aristas[(v_ini,vecino2)]:
        vecino1 = vecino2
    q.push(vecino1)
    seen.add(vecino1)

    while len(vertices) != len(g.V):
        v = q.pop()
        vertices.append(v)

        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                q.push(suc)

    return vertices

if __name__ == '__main__':
    nr_puntos, puntos = load_file2()
    aristas, aristas_buenas = create_graph(puntos)
    aristas2 = dict()
    for e, w in aristas_buenas:
        aristas2[e] = w
    # print("Aristas2 ",aristas2.items())


    # kruskal_path = kruskal(aristas2, g)
    # print(kruskal_path)
    kruskal_path2 = kruskal2(aristas)
    print(kruskal_path2)
    g = UndirectedGraph(E=kruskal_path2)
    print(kruskal_final(g,0,aristas))
    # check_distance(aristas, kruskal_path)
    # print(shortest_edge(aristas,3,0))
    # create_graph2(puntos)
    # print(orden(sorted(aristas.items(), key=lambda x: x[1])))

from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from algoritmia.datastructures.mergefindsets import MergeFindSet
from typing import *
import sys
import math

from algoritmia.datastructures.queues import Fifo
from algoritmia.utils import infinity

Vertex = TypeVar('Vertex')
Edge = Tuple[int,int]

def load_file():
    nr_puntos = 0
    puntos = []
    listaVertices = []

    try:
        nr_puntos = sys.stdin.readline()

        for line in sys.stdin.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)

        for i in range(len(puntos)):
            listaVertices.append(i)

    except IOError:
        print("File cannot be open!")
    return nr_puntos, puntos, listaVertices

def load_file2():
    nr_puntos = 0
    puntos = []
    listaVertices = []

    try:
        f = open(sys.argv[1])
        nr_puntos = f.readline()

        for line in f.readlines():
            x1, y1 = line.split(" ")
            punto = (float(x1), float(y1))
            puntos.append(punto)

        for i in range(len(puntos)):
            listaVertices.append(i)

    except IOError:
        print("File cannot be open!")
    return nr_puntos, puntos, listaVertices

def euclidean_distance(x, y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]

    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def kruskal(puntos, listaVertices):
    distancia = set()
    for i in listaVertices:
        for x in listaVertices:
            if x != i:
                distancia.add((euclidean_distance(puntos[i], puntos[x]), (i, x)))
    pesos_ordenados = sorted(distancia, key=lambda i:i)
    mfs: MergeFindSet[Vertex] = MergeFindSet()
    for v in listaVertices:
        mfs.add(v)

    limite = [2] * len(puntos)
    weight = 0
    aristas: List[Edge] = []

    for peso,arista in pesos_ordenados:
        if limite[arista[0]] > 0 and limite[arista[1]] > 0:
            if mfs.find(arista[0]) != mfs.find(arista[1]):
                mfs.merge(arista[0],arista[1])
                aristas.append(arista)
                limite[arista[0]] -= 1
                limite[arista[1]] -= 1
                weight += peso
    vertice_extra = []
    for i, x in enumerate(limite):
        if x == 1:
            vertice_extra.append(i)
    aristas.append(tuple(vertice_extra))
    return UndirectedGraph(E=aristas), weight, limite


def prim(v_ini, puntos, listaVertices):
    aristas_g = []
    for i in listaVertices:
        for x in listaVertices:
            if x != i:
                aristas_g.append((i,x))

    g = UndirectedGraph(E=aristas_g)

    seen = set()
    weight = 0
    seen.add(v_ini)
    aristasVisitadas = []
    limite = [2] * len(puntos)

    while len(seen) != len(g.V):
        listaDistancias = []
        for x in seen:
            for suc in g.succs(x):
                if suc not in seen and limite[x] > 0 and limite[suc] > 0:
                    dist = euclidean_distance(puntos[x],puntos[suc])
                    listaDistancias.append((dist,(x,suc)))

        minimo = min(listaDistancias)
        weight += minimo[0]
        aristasVisitadas.append(minimo[1])
        seen.add(minimo[1][1])
        limite[minimo[1][0]] -= 1
        limite[minimo[1][1]] -= 1

    return UndirectedGraph(E=aristasVisitadas), weight, limite

def recorredor_aristas_anchura(g:UndirectedGraph, v_inicial: int) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial,v_inicial))
    seen.add(v_inicial)

    while len(queue)>0:
        u,v = queue.pop()
        aristas.append((u,v))
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v,suc))

    return aristas

def recuperador_camino(lista_aristas:List[Edge], v:int) -> List[int]:
    bp = {}

    for orig,dest in lista_aristas:
        bp[dest] = orig
    camino = []
    camino.append(v)

    while v != bp[v]:
        v = bp[v]
        camino.append(v)

    return camino

if __name__ == '__main__':
    nr_puntos, puntos, listaVertices = load_file2()
    kruskal, peso, limite = kruskal(puntos,listaVertices)

    prim, peso_p, limite_p = prim(0,puntos,listaVertices)

    inicio = 0
    inicio_final = []

    for i in range(len(limite)):
        if limite[i] == 1:
            inicio_final.append(i)

    x,y = inicio_final
    peso += euclidean_distance(puntos[x],puntos[y])
    print(kruskal)
    camino = recuperador_camino(recorredor_aristas_anchura(kruskal,x), y)
    print(peso)
    print(camino)

    inicio_p = 0
    inicio_final_p = []

    for i in range(len(limite_p)):
        if limite_p[i] == 1:
            inicio_final_p.append(i)

    x_p, y_p = inicio_final_p
    peso_p += euclidean_distance(puntos[x_p], puntos[y_p])

    camino_p = recuperador_camino(recorredor_aristas_anchura(prim, x_p), y_p)
    print(camino_p)
    print(peso_p)
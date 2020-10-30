from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

from labyrinthviewer import LabyrinthViewer

Vertex = TypeVar('Vertex')  # Tipo generico (Java <T>)
Edge = Tuple[Vertex, Vertex]


# recorrido en anchura de las aristas
# es lo mismo que el recorrido de aristas solo que devolvemos un array de aristas

def edge_path(lab: UndirectedGraph, v_ini: Vertex) -> List[Vertex]:
    seen = set()
    aristas = []

    def explorar_desde(u, v):
        seen.add(v)
        aristas.append((u, v))

        for suc in lab.succs(v):
            if suc not in seen:
                explorar_desde(v, suc)

    explorar_desde(v_ini, v_ini)
    return aristas


# v es el vertice al cual queremos llegar
def recuperador_camino(lista_aristas, v):
    bp = {}

    for orig, dest in lista_aristas:
        bp[dest] = orig
    # reconstruir camino hacia atras
    camino = [v]

    while v != bp[v]:
        v = bp[v]
        camino.append(v)

    camino.reverse()
    return camino



if __name__ == '__main__':
    pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
                ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
                ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

    lab = UndirectedGraph(E=pasillos)
    v_ini = (0, 0)
    v_tes = (1, 3)

    print(edge_path(lab, v_ini))

    camino = recuperador_camino(edge_path(lab, v_ini), v_tes)
    print("Camino al v_tes {0}".format(camino))

    lv = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)
    lv.add_path(camino)
    lv.run()

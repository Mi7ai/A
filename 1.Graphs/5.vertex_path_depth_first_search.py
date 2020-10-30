from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = TypeVar('Vertex')  # Tipo generico (Java <T>)


# recorrido en anchura de los vertices
# es lo mismo que el recorrido de vertices solo que devolvemos un array de vertices

def vertex_path(lab: UndirectedGraph, v_ini: Vertex) -> List[Vertex]:
    seen = set()
    vertices = []

    def explorar_desde(v):
        seen.add(v)
        vertices.append(v)

        for suc in lab.succs(v):
            if suc not in seen:
                explorar_desde(suc)

    explorar_desde(v_ini)
    return vertices


if __name__ == '__main__':
    pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
                ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
                ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

    lab = UndirectedGraph(E=pasillos)
    v_ini = (0, 0)

    print(vertex_path(lab, v_ini))

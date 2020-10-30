from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = TypeVar('Vertex')  # Tipo generico (Java <T>)


# recorrido en anchura de los vertices
# es lo mismo que el recorrido de vertices solo que devolvemos un array de vertices

def vertex_path(lab: UndirectedGraph, v_ini: Vertex) -> List[Vertex]:
    q = Fifo()
    seen = set()
    vertices = []

    q.push(v_ini)
    seen.add(v_ini)

    while len(q) > 0:
        at = q.pop()
        vertices.append(at)

        for suc in lab.succs(at):
            if suc not in seen:
                seen.add(suc)
                q.push(suc)

    return vertices


if __name__ == '__main__':
    pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
                ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
                ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

    lab = UndirectedGraph(E=pasillos)
    v_ini = (0, 0)

    print(vertex_path(lab, v_ini))

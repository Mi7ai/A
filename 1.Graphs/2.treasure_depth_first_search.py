from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = Tuple[int, int]


def dfst(lab, v_ini, v_tes):
    seen = set()

    def explorar_desde(v):
        seen.add(v)

        if v == v_tes:
            return v
        for suc in lab.succs(v):
            if suc not in seen:
                res = explorar_desde(suc)  # devuelve none si no encuentra el vertice tesoro entre sus ultimos vecinos

                if res is not None:
                    return res

    return explorar_desde(v_ini)


# para hacer el mismo algoritmo recursivo creo que no se puede. es mejor con recursividad


if __name__ == '__main__':
    pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
                ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
                ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

    lab = UndirectedGraph(E=pasillos)
    v_ini = (0, 0)
    v_tes = (1, 3)

    pos = dfst(lab, v_ini, v_tes)

    if pos is None:
        print("Tesoro no encontrado")
    else:
        print("Tesoso encontrado en el vertice {0}".format(pos))

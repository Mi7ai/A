from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo


# busqueda tesoro en anchura

def bfst(lab, v_ini, v_tes):
    q = Fifo()
    seen = set()

    q.push(v_ini)
    seen.add(v_ini)

    while len(q) > 0:
        at = q.pop()
        if v_tes == at:
            return at

        for suc in lab.succs(at):
            if suc not in seen:
                seen.add(suc)
                q.push(suc)

    return None


if __name__ == '__main__':
    pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
                ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
                ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

    lab = UndirectedGraph(E=pasillos)
    v_ini = (0, 0)
    v_tes = (1, 3)

    pos = bfst(lab, v_ini, v_tes)

    if pos is None:
        print("Tesoro no encontrado")
    else:
        print("Tesoso encontrado en el vertice {0}".format(pos))

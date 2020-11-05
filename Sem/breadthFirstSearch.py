from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = TypeVar('Vertex')


class BreadthFirstSearch:
    def __init__(self, graph: UndirectedGraph, v_ini: Vertex):
        self.graph = graph
        self.v_ini = v_ini
        self.q = Fifo()
        self.seen = set()
        self.q.push((v_ini, v_ini))
        self.seen.add(v_ini)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.q) == 0:
            raise StopIteration
        u, v = self.q.pop()
        for suc in self.graph.succs(v):
            if suc not in self.seen:
                self.seen.add(suc)
                self.q.push((v, suc))
        return u, v


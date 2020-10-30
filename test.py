from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import LabyrinthViewer
from random import shuffle


__author__ = "Mihai"
__status__ = "Finished"

# creates a labyrinth with given rows and cols size


def create_labyrinth(rows, cols):
    # general expressions of all vertexes
    vertices = [(row, col) for row in range(rows) for col in range(cols)]

    mfs = MergeFindSet()
    edges = []

    for v in vertices:
        # print(v)
        mfs.add(v)

    # add the bottom row and right column to edge list and shuffle it
    for row, col in vertices:
        if row+1 < rows:
            edges.append([(row, col), (row+1, col)])
        if col+1 < cols:
            edges.append([(row, col), (row, col+1)])
    shuffle(edges)
    # # #
    # for i in edges:
    #     a, b = i
    #     print(a, b)
    ###

    corridors = []

    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    for u, v in corridors:
        print("Path: {} -> {}".format(u, v))

    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    lab = create_labyrinth(10, 15)
    LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10).run()

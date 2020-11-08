from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from labyrinthviewer import LabyrinthViewer
import tkinter as tk
from typing import *
import random

Vertex = TypeVar('Vertex')


def create_labyrinth(rows, cols):
    # vertex creation
    vertexes = [(row, col) for row in range(rows) for col in range(cols)]

    mfs = MergeFindSet()
    edges = []

    for v in vertexes:
        mfs.add(v)

    # add bottom row and right column to the edge list and shuffle
    for row, col in vertexes:
        if row + 1 < rows:
            edges.append(((row, col), (row + 1, col)))
        if col + 1 < cols:
            edges.append(((row, col), (row, col + 1)))

    random.shuffle(edges)

    corridors = []

    # create corridors list
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return corridors


def execute_maze(*args):
    lab = UndirectedGraph(E=create_labyrinth(int(rowsInput.get()), int(colsInput.get())))
    lv = LabyrinthViewer(lab, canvas_width=1000, canvas_height=1000, margin=10)
    lv.run()


if __name__ == '__main__':
    root = tk.Tk()
    # window width x window height + position right + position down from (0,0)
    root.geometry("500x100+1800+100")
    # Rows Label and Entry box
    rowsLabel = tk.Label(root, text="Labyrinth Rows")
    rowsLabel.grid(row=0, column=0)
    rowsInput = tk.Entry(root)
    rowsInput.grid(row=0, column=1)

    # Cols Label and Entry box
    colsLabel = tk.Label(root, text="Labyrinth Cols")
    colsLabel.grid(row=1, column=0)
    colsInput = tk.Entry(root)
    colsInput.grid(row=1, column=1)

    button1 = tk.Button(root, text="Create Maze", bg='palegreen2')
    button1.bind("<Button-1>", execute_maze)
    button1.grid(row=2, column=1, columnspan=2)

    root.mainloop()
